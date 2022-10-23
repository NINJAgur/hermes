# Generated by Django 3.2.13 on 2022-10-20 18:48

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_rename_manual_manual_man_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manual',
            name='man_file',
            field=models.FileField(blank=True, null=True, upload_to='apps/static/assets/upload-manuals/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['doc', 'docx', 'pdf', 'txt', 'ppt', 'pptx'])]),
        ),
    ]