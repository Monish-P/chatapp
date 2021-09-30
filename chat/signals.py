from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile,Message,Notification,Group,Room

@receiver(post_save, sender=User,dispatch_uid='create_profile')
def create_profile(sender, instance, created, **kwargs):
    if created:
       p = Profile.objects.create(user=instance)
       p.save()


@receiver(post_save, sender=Message,dispatch_uid='get_notification')
def get_notification(sender, instance, created, **kwargs):
    r = Room.objects.get(id=instance.room)
    if created and Group.objects.filter(name=r.name,user=instance.user).exists():
        if Notification.objects.filter(user=r.name).exists():
            pass
        else:
            n = Notification.objects.create(user=r.name)
            n.save()
    else:
        if Notification.objects.filter(user=instance.user).exists():
            pass
        else:
            n = Notification.objects.create(user=instance.user)
            n.save()
