# Generated by Django 3.2.6 on 2021-09-21 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0011_message_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='image',
            field=models.ImageField(upload_to='chat_imgs'),
        ),
    ]
