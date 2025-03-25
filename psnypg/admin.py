from django.contrib import admin
# Register your models here.
from . import models
from .models import ExcosPicturePost

#The DeusMagnus main post model admin
class ExcosPicturePostModelAdmin (admin.ModelAdmin):
    list_display = ['excos_img','excos_author']
admin.site.register(ExcosPicturePost, ExcosPicturePostModelAdmin)