# Generated by Django 4.1.5 on 2023-04-27 20:24

import catalog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_alter_customuser_profile_photo_circle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='profile_photo',
            field=models.ImageField(blank=True, default='static/images/design/login_icon.svg', null=True, upload_to=catalog.models.user_profile_photo_directory_path),
        ),
    ]