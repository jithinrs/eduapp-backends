from asgiref.sync import async_to_sync
from channels.generic.websocket import JsonWebsocketConsumer
from django.db.models import Q

from Authentications.models import Account
from .models import Conversation,Message
from .serializer import MessageSerializer

class ChatConsumer(JsonWebsocketConsumer):
    """
    This consumer is used to show user's online status,
    and send notifications.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.user = None
        self.conversation_name = None
        self.conversation = None
        self.new_name = None

    def connect(self):
        user_id = self.scope["user_id"]
        # print(user_id)
        try:
            self.user = Account.objects.get(id = user_id)
        except:
            return
        print("Connected!")
        self.accept()
        self.conversation_name = f"{self.scope['url_route']['kwargs']['conversation_name']}"
        self.conversation, created = Conversation.objects.get_or_create(name=self.conversation_name)
        async_to_sync(self.channel_layer.group_add)(
            self.conversation_name,
            self.channel_name,
        )
        # self.send_json(
        #     {
        #         "type": "welcome_message",
        #         "message": "Hey there! You've successfully connected!",
        #     }
        # )
        old_name = self.conversation_name
        name_split = old_name.split("__")
        new_name = name_split[1] + "__" + name_split[0]

       
        # messages = self.conversation.messages.all().order_by("-timestamp")[0:50]
        test = Conversation.objects.filter(Q(name = new_name)| Q(name = old_name)).values('id')
        messages = Message.objects.filter(conversation__in = test).order_by("-timestamp")[0:50]
        
        print(test)
        print(messages)
        self.send_json({
            "type": "last_50_messages",
            "messages": MessageSerializer(messages, many=True).data,
        })

    def disconnect(self, code):
        print("Disconnected!")
        return super().disconnect(code)

    def get_receiver(self):
        sender, reciever = self.conversation_name.split("__")
        recieverId = Account.objects.get(id = reciever)
        return recieverId

    def receive_json(self, content, **kwargs):
        message_type = content["type"]
        if message_type == "chat_message":
            print(self.user, self.get_receiver())
            message = Message.objects.create(
                from_user=self.user,
                to_user=self.get_receiver(),
                content=content["message"],
                conversation=self.conversation
            )
            async_to_sync(self.channel_layer.group_send)(
                self.conversation_name,
                {
                    "type": "chat_message_echo",
                    "name": content["name"],
                    "message": MessageSerializer(message).data,
                },
            )
            # async_to_sync(self.channel_layer.group_send)(
            #     self.new_name,
            #     {
            #         "type": "chat_message_echo",
            #         "name": content["name"],
            #         "message": MessageSerializer(message).data,
            #     },
            # )
        return super().receive_json(content, **kwargs)

    def chat_message_echo(self, event):
        print(event)
        self.send_json(event)