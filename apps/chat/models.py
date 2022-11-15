from django.contrib.auth.models import User
from django.db import models
import datetime

class Room(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    updated = models.DateField(auto_now_add=True)
    lastMessage = models.CharField(blank=True,max_length=255)
    
    def updateDate(self):
        self.updated = datetime.date.today()

class Message(models.Model):
    room = models.ForeignKey(Room, related_name='messages', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='messages', on_delete=models.CASCADE)
    content = models.TextField()
    date_added = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ('date_added',)