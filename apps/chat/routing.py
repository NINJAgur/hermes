from django.urls import path

from . import consumers

websocket_urlpatterns = [
    path('ms/<str:room_name>/', consumers.ChatConsumer.as_asgi()),
    path('ws/<str:room_name>/', consumers.ChatConsumer.as_asgi()),
]