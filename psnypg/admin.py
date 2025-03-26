from django.contrib import admin
# Register your models here.
from . import models
from .models import ExcosPicturePost,MainHeaderPicturePost,LogoPicturePost

#The main header picture post model admin
class MainHeaderPicturePostModelAdmin (admin.ModelAdmin):
    prepopulated_fields = {'main_header_slug': ('main_header_title',)}
    list_display = ['main_header_title','main_header_img','main_header_description']
admin.site.register(MainHeaderPicturePost, MainHeaderPicturePostModelAdmin)

# the excos caroseul picture
class ExcosPicturePostModelAdmin (admin.ModelAdmin):
    list_display = ['excos_img','excos_author']
admin.site.register(ExcosPicturePost, ExcosPicturePostModelAdmin)

# the Logo caroseul picture
class LogoPicturePostModelAdmin (admin.ModelAdmin):
    list_display = ['logo_img','logo_author']
admin.site.register(LogoPicturePost, LogoPicturePostModelAdmin)