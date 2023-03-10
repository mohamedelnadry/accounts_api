from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User ,on_delete=models.CASCADE)
    bio = models.TextField()
    birthdate = models.DateField(auto_now=False, auto_now_add=False)
    # avatar = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)

    def __str__(self):
        return str(self.user.username)
    