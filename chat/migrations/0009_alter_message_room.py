# Generated by Django 3.2.6 on 2021-09-19 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0008_alter_message_room'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='room',
            field=models.CharField(max_length=1000000),
        ),
    ]
