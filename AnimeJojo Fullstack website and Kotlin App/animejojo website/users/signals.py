from django.core import signals
from django.dispatch import receiver
from django.db.models.signals import post_save,post_delete
from django.contrib.auth.models import User
from .models import Profile

@receiver(post_save,sender = User)
def createProfile(sender,created,instance,**kwargs):
    if created:
        owner = instance
        profile = Profile.objects.create(
            user = owner,
            first_name = owner.first_name,
            last_name = owner.last_name,
            username = owner.username,
            email = owner.email,
        )

# @receiver(post_delete,sender = Profile)
# def deleteProfile(sender,instance):