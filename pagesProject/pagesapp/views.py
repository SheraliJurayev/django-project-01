from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class HomeView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'

class LikePageView(TemplateView):
    template_name='like.html'

class FollowPageView(TemplateView):
    template_name='follow.html'