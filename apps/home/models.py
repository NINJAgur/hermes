from operator import truediv
from os import system
from django.db import models
from django.db.models import PositiveIntegerField
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User
import uuid

# Create your models here.

class Record(models.Model):
    AIRPORT = 'AIRPORT'
    BE = 'BE'

    CHOICES_SYSTEM = (
        (AIRPORT, 'AIRPORT'),
        (BE, 'BE')
    )


    FINISHED = 'FINISHED'
    IN_PROGRESS = 'IN PROGRESS'
    ABORTED = 'ABORTED'

    CHOICES_STATUS = (
        (FINISHED, 'FINISHED'),
        (IN_PROGRESS, 'IN PROGRESS'),
        (ABORTED, 'ABORTED')
    )

    id = models.AutoField(default=0, primary_key=True)
    record_id =  models.UUIDField(default=uuid.uuid4, editable=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    
    system_type = models.CharField(max_length=20, choices=CHOICES_SYSTEM, default=AIRPORT)
    status = models.CharField(max_length=20, choices=CHOICES_STATUS, default=IN_PROGRESS)
    network = models.CharField(max_length = 12)
    date_start = models.DateField()
    date_finish = models.DateField(blank=True)
    
    progression = PositiveIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])

    short_description = models.TextField(blank=True, null=True)
    long_description = models.TextField(blank=True, null=True)
    short_solution = models.TextField(blank=True, null=True)
    long_solution = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.record_id)