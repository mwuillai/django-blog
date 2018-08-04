from django.contrib import admin
from .models import Users, Articles, Comments

# Register your models here.
admin.site.register(Users)
admin.site.register(Articles)
admin.site.register(Comments)
