from django.contrib import admin
# Register your models here.
from . import models
from .models import WhyPSNYPG,PsnypgNewsAndEvent
from .models import ExcosPicturePost,MainHeaderPicturePost,LogoPicturePost,ExcosUser


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


#The main excos post model admin
class ExcosUserPostModelAdmin (admin.ModelAdmin):
    prepopulated_fields = {'excos_user_slug': ('excos_user_name',)}
    list_display = ['excos_user_name','excos_user_email','excos_user_whatsapp_number']
admin.site.register(ExcosUser, ExcosUserPostModelAdmin)

#WhyPSNYPG
class WhyPSNYPGPostModelAdmin (admin.ModelAdmin):
    prepopulated_fields = {'why_psnypg_slug': ('why_psnypg_title',)}
    list_display = ['why_psnypg_title','why_psnypg_description','why_psnypg_publish_date']
admin.site.register(WhyPSNYPG, WhyPSNYPGPostModelAdmin)

#Psnypg News And Event
class PsnypgNewsAndEventPostModelAdmin (admin.ModelAdmin):
    prepopulated_fields = {'psnypg_news_and_event_slug': ('psnypg_news_and_event_title',)}
    list_display = ['psnypg_news_and_event_title','psnypg_news_and_event_img','psnypg_news_and_event_description']
admin.site.register(PsnypgNewsAndEvent, PsnypgNewsAndEventPostModelAdmin)