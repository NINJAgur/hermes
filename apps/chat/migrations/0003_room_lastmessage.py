# Generated by Django 3.2.13 on 2022-11-04 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_auto_20221104_1847'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='lastMessage',
            field=models.CharField(default='test', max_length=255),
            preserve_default=False,
        ),
    ]
