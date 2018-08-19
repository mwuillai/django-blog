from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    newsletter = models.BooleanField(default=False)
    location = models.DateField(null=True, blank=True)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class Articles(models.Model):
    title = models.CharField(max_length=200)
    title2 = models.CharField(max_length=400)
    article = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='blog/static/blog/article_image')
    creation_date = models.DateTimeField(auto_now_add=True)


class Comments(models.Model):
    comment = models.TextField(blank=True, null=True)
    user_id = models.ForeignKey(Profile, on_delete=models.CASCADE)
    article_id = models.ForeignKey(Articles, on_delete=models.CASCADE)
    creation_date = models.DateTimeField(auto_now_add=True)
