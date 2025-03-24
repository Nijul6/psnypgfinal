from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Make root URL go to index
    path('index/', views.index, name='index'),
    # other URL patterns...
]
