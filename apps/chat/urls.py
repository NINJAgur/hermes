from django.urls import path, re_path
from apps.chat import views

urlpatterns = [

    path('', views.render_chat, name='chat'),
]
