from django.urls import path
from .consumers import chatconsumer

websocket_urlpatterns = [
    path('ws/chat/<str:room_name>/',chatconsumer.as_asgi())
]