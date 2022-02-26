from django.db import models
from django.contrib.auth.models import User
import uuid

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=90, null=False, blank=False, default='first-name')
    last_name = models.CharField(max_length=90, null=False, blank=False, default='last-name')
    username = models.CharField(max_length=90, null=False, blank=False, default='username')
    email = models.EmailField(null=True, blank=True)
    display_picture = models.ImageField(default='user.svg')
    bio = models.TextField(blank=True,null=True)
    dob = models.DateTimeField(blank=True, null=True)
    stamp = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(editable=False, unique=True, primary_key=True, default=uuid.uuid4)

    def __str__(self) -> str:
        return self.username

