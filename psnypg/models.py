from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date

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
