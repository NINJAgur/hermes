# Generated by Django 3.2.13 on 2022-11-19 16:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0005_room_isprivate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='isPrivate',
        ),
    ]