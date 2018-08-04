from django.db import models
from django.utils import timezone


class Users(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)
    newsletter = models.BooleanField(default=False)
    registration_date = models.DateTimeField(auto_now_add=True)


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
