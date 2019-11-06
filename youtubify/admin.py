from django.contrib import admin
from .models import User, Video
# Register your models here.
admin.site.register([User, Video])