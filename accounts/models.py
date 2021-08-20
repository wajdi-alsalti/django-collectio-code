from django.db import models
# import the user from django is built in 
# the same user in admin 
from django.contrib.auth.models import User

# to create profile for the user
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.

# create profile class
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='user_profile',default='/default/defaultImg.png')
    phone_number = models.CharField(max_length=25)

    def __str__(self):
        return str(self.user)


# create new user --> create new empty profile
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

