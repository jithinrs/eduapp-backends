from django.urls import path
from .consumers import ChatConsumer

from .views import *
urlpatterns = [
    path('allusers', ChatUsersAll.as_view()),
    path("chats/<slug>/", ChatConsumer.as_asgi()),
]