from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Make root URL go to index
    # other URL patterns...
]
