from django.urls import path
from apps.chat import views

urlpatterns = [
    path('', views.rooms, name='rooms'),
    path('<slug:slug>/', views.rooms_id, name='rooms_id'),
    path('rooms/<slug:slug>', views.room, name='room'),
    path('get-chat/<slug:slug>', views.get_chat_room, name='get-chat')
]