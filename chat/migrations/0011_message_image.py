# Generated by Django 3.2.6 on 2021-09-21 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0010_profile_is_online'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='image',
            field=models.ImageField(null=True, upload_to='chat_imgs'),
        ),
    ]
