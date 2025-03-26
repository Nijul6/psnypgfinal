from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView,ListView
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.urls import reverse
from django.urls import reverse_lazy
from .models import ExcosPicturePost,MainHeaderPicturePost,LogoPicturePost,ExcosUser
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin  


def index (request):
    return render (request, 'psnypg/index.html')

#The main HomeView page
class HomeView(ListView): 
    model = ExcosPicturePost
    template_name = 'psnypg/home.html'
    
    def get_context_data(self, **kwargs):  
        context = super().get_context_data(**kwargs)
        context['first_main_header_pictures'] = MainHeaderPicturePost.objects.all()  
        context['logo_sponsors'] = LogoPicturePost.objects.all()
 
        return context

    
def whoWeAre (request):
    return render (request, 'psnypg/who_we_are.html')

def whatWeDo (request):
    return render (request, 'psnypg/what_we_do.html')

def WhyPsn (request):
    return render (request, 'psnypg/why_psn.html')

def OurImpact (request):
    return render (request, 'psnypg/our_impact.html')

def Dala2025 (request):
    return render (request, 'psnypg/dala_2025.html')

def Contact_Us (request):
    return render (request, 'psnypg/contact.html')

# Excos User page
class ExcosUserPage(ListView): 
    model = ExcosUser
    template_name = 'psnypg/excos_user.html'
    def ExcosUserPage (request):
        return render(request, 'psnypg/excos_user.html', {})