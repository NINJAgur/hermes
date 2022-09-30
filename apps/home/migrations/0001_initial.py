# Generated by Django 3.2.13 on 2022-09-26 20:35

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(default=0, primary_key=True, serialize=False)),
                ('record_id', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('system_type', models.CharField(choices=[('AIRPORT', 'AIRPORT'), ('BE', 'BE')], default='AIRPORT', max_length=20)),
                ('status', models.CharField(choices=[('FINISHED', 'FINISHED'), ('IN PROGRESS', 'IN PROGRESS'), ('ABORTED', 'ABORTED')], default='IN PROGRESS', max_length=20)),
                ('network', models.CharField(max_length=12)),
                ('date_start', models.DateField()),
                ('date_finish', models.DateField(blank=True)),
                ('progression', models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('short_description', models.TextField(blank=True, null=True)),
                ('long_description', models.TextField(blank=True, null=True)),
                ('short_solution', models.TextField(blank=True, null=True)),
                ('long_solution', models.TextField(blank=True, null=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]