from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView,ListView
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.urls import reverse
from django.urls import reverse_lazy
from .models import ExcosPicturePost,MainHeaderPicturePost,LogoPicturePost,ExcosUser,WhyPSNYPG,PsnypgNewsAndEvent
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

def OurImpact (request):
    return render (request, 'psnypg/our_impact.html')

def Dala2025 (request):
    return render (request, 'psnypg/dala_2025.html')

def DalaYps (request):
    return render (request, 'psnypg/dala_yps.html')

def Nafdac_Yada (request):
    return render (request, 'psnypg/nafdac_yada.html')

def Why_Nafdac (request):
    return render (request, 'psnypg/why_nafdac_yada.html')


'''def WhyPsn (request):
    return render (request, 'psnypg/why_psn.html')'''

#This Why_Psnypg view
class Why_Psnypg(ListView):
    model = WhyPSNYPG
    template_name = 'psnypg/why_psn.html'

#The why psnypg article details class base view
class WhyPsnypgArticleDetailView(DetailView):
    model = WhyPSNYPG
    template_name = 'psnypg/why_psn_article.html'
    def WhyPsnypgArticleDetailView(request, pk): 
        object = get_object_or_404(WhyPSNYPG, pk=pk)
        return render(request, 'psnypg/why_psn_article.html',{'whypsn_article_detail': object})
    

def Contact_Us (request):
    return render (request, 'psnypg/contact.html')

# Excos User of the PSNYPG
class ExcosUserPage(ListView):
    model = ExcosUser
    template_name = 'psnypg/excos_user.html'
    context_object_name = 'excos_users'

    def get_queryset(self):
        email = self.kwargs.get('email')  # Get email from the URL
        if email:
            return ExcosUser.objects.filter(excos_user_email=email)  # Show specific user by email
        return ExcosUser.objects.all()  # Show all users if no email is provided
    
#The Excos User  article details class base view
class ExcosUserArticleDetailView(DetailView):
    model = ExcosUser
    template_name = 'psnypg/excos_users_article.html'
    def ExcosUserArticleDetailView(request, pk): 
        object = get_object_or_404(ExcosUser, pk=pk)
        return render(request, 'psnypg/excos_users_article.html',{'excos_users_article': object})
    
    
def News_Update (request):
    return render (request, 'psnypg/news_update.html')

class Psnypg_News_And_Event(ListView):
    model = PsnypgNewsAndEvent
    template_name = 'psnypg/news_update.html'