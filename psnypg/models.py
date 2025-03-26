from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date

#The main header logo of the page
class MainHeaderPicturePost(models.Model):
    main_header_title = models.CharField(max_length=255, blank=True, null=True)
    main_header_description = models.TextField()
    main_header_slug = models.SlugField (max_length=255,blank=True, null=True)
    main_header_img = models.ImageField(upload_to='main_images/')
    main_header_excos_publish_date = models.DateTimeField(auto_now_add=True)
    main_header_excos_author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['main_header_excos_publish_date']
        
    def __str__(self):
        return self.main_header_title + ' | ' + str(self.main_header_excos_author)

    def get_absolute_url(self):
        return reverse('home',)
    

#The logo page of sponsor
class LogoPicturePost(models.Model):
    logo_img = models.ImageField(upload_to='logo_images/')
    logo_publish_date = models.DateTimeField(auto_now_add=True)
    logo_author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['logo_publish_date']
    
    def __str__(self):
        return f"Post by {self.logo_author.username}"

    def get_absolute_url(self):
        return reverse('home',)
    
    
class ExcosPicturePost(models.Model):
    excos_img = models.ImageField(upload_to='images/')
    excos_publish_date = models.DateTimeField(auto_now_add=True)
    excos_author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['excos_publish_date']
    
    def __str__(self):
        return f"Post by {self.excos_author.username}"  # Return string-based representation
    
    def get_absolute_url(self):
        return reverse('index',)
    
#Excos full details model
class ExcosUser(models.Model):
    excos_user_name = models.CharField(max_length=255)
    excos_user_description = models.TextField()
    excos_user_slug = models.SlugField (max_length=255,blank=True, null=True)
    excos_user_email = models.EmailField(max_length=255)
    excos_user_whatsapp_number = models.CharField(max_length=15)
    excos_user_url = models.URLField(max_length=255, blank=True, null=True)  # LinkedIn URL field
    excos_user_publish_date = models.DateTimeField(auto_now_add=True)
    excos_user_author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    class Meta:
        ordering = ['excos_user_publish_date']

    def __str__(self):
        return self.excos_user_name