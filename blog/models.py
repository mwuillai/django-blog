from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Profile(models.Model):
    """Mettre à jour cette classe pour enrichir la classe par défaut de django
    plutôt que de créer une nouvelle table utilisateur"""
    user= models.OneToOneField(User, on_delete=models.CASCADE)
    newsletter = models.BooleanField(default=False)
    registration_date = models.DateTimeField(auto_now_add=True)
    bio = models.CharField(max_length=30, blank=True)
    birth_date=models.DateField(null=True, blank=True)

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
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    article_id = models.ForeignKey(Articles, on_delete=models.CASCADE)
    creation_date = models.DateTimeField(auto_now_add=True)
