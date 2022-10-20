from django.contrib import admin
from . models import Record, Update, Manual

# Register your models here.
admin.site.register(Record)
admin.site.register(Update)
admin.site.register(Manual)