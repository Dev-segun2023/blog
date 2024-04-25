from django.db.models.signals import post_save
from base.models import User
from django.dispatch import receiver
from .models import profile


@receiver(post_save, sender=User)
def create_Profile(sender,instance,created,**kwargs):
    if created:
        profile.objects.create(user=instance)




@receiver(post_save, sender=User)
def save_Profile(sender,instance,**kwargs):
    instance.profile.save()