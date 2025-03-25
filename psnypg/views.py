from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView,ListView
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.urls import reverse
from django.urls import reverse_lazy
from .models import ExcosPicturePost
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin  


def index (request):
    return render (request, 'psnypg/index.html')

#The main HomeView page
class HomeView(ListView): 
    model = ExcosPicturePost
    template_name = 'psnypg/home.html'
    def HomeView (request):
        return render(request, 'psnypg/home.html', {})