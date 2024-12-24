# Generated by Django 5.1.3 on 2024-12-24 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_remove_profile_image_profile_avatar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='avatar',
        ),
        migrations.AddField(
            model_name='profile',
            name='avatar_id',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
