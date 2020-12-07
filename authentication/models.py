from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class Profile(models.Model):

    user = models.OneToOneField(User, on_delete = models.CASCADE)
    avatar = models.ImageField(default = 'djangoAvatar.jpg', upload_to = 'profile_pictures') #stores image url

    def __str__(self):
        return  self.user.username

        #Run this function every time a User is created
    @receiver(post_save, sender = User)
    def create_profile(sender, instance, created, **kwargs):
        if created: #if User was created
            Profile.objects.create(user = instance)

    @receiver(post_save, sender = User)
    def save_profile(sender, instance, **kwargs):
        instance.profile.save()
