from django.contrib import admin
from .models import Profile, Articles, Comments

# Register your models here.
admin.site.register(Profile)
admin.site.register(Articles)
admin.site.register(Comments)
