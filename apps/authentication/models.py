from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class UserHermes(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    #phone_number = models.CharField(max_length=10)
    phone_number = PhoneNumberField(unique=True, blank=True, null=True)
    office = models.CharField(max_length=10, blank=True, null=True)
    
    def __str__(self):
        return self.user.username
