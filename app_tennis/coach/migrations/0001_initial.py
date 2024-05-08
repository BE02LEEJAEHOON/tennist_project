# Generated by Django 5.0.4 on 2024-05-04 22:57

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('club', '0002_alter_club_image_url'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Coach',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('club', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='club.club')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'coach',
            },
        ),
    ]