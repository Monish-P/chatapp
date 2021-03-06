# Generated by Django 3.2.6 on 2021-09-21 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0014_alter_message_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='image',
            field=models.ImageField(blank=True, default='', upload_to='chat_imgs'),
        ),
        migrations.AlterField(
            model_name='message',
            name='value',
            field=models.CharField(blank=True, max_length=1000000),
        ),
    ]
