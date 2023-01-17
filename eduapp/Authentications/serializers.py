from rest_framework import serializers
from .models import Account, teste


# class Testserializer(serializers.ModelSerializer):
#     class Meta:
#         model = teste
#         fields = ['nametest','findname']


class AuthenticationSerializer(serializers.ModelSerializer):

    # testerrr = Testserializer(many = True)
    class Meta:
        model = Account
        fields=['first_name','last_name' ,'email','mobile','gender', 'date_of_birth' ,'password','roles']
    
    def create(self, validated_data):
        # hashing password
        password = validated_data.pop('password')
        # testing = validated_data.pop('testerrr')
        user = super().create(validated_data)
        if user.roles == "S":
            user.verified_role = True
        # for test in testing:
        #     teste.objects.create(user_id = user, **test)
        user.set_password(password)
        user.save()



        return user
