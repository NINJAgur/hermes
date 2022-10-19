from django.db import models

# Create your models here.

class CustomUser(models.Model):
    name = models.CharField(max_length=8)
    active = models.BooleanField(default=False)


    def __str__(self):
        return self.name



