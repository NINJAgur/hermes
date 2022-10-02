# Generated by Django 3.2.13 on 2022-10-01 19:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0004_update_published_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='update',
            name='published',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='update',
            name='published_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]