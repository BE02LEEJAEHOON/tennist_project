# Generated by Django 5.0.5 on 2024-05-08 13:01

import image_url.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image_url', '0010_remove_imageurl_content_type_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='imageurl',
            name='image_file',
            field=models.ImageField(blank=True, null=True, storage=image_url.models.InMemoryUploadStorage(), upload_to='temp/'),
        ),
    ]