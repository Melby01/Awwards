# Generated by Django 3.2.5 on 2021-07-20 13:31

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Awww', '0002_alter_profile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='image',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='images/'),
        ),
    ]
