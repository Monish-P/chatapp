# Generated by Django 3.2.6 on 2021-09-28 04:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chat', '0018_alter_notification_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000000)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Group', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
