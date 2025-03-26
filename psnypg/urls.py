
from django.urls import path
from . import views
from .views import HomeView

urlpatterns = [
    #path('', views.index, name='index'),  # Make root URL go to index
    # other URL patterns...
    path('', HomeView.as_view(), name="home"),
    path('home/', HomeView.as_view(), name='home'),
    path('whoweare/', views.whoWeAre, name='whoweare'),
    path('contact_us/', views.Contact_Us, name='contact_us'),
]
