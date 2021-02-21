from django.shortcuts import render

# Create your views here.

# pages/view.py
from django.views.generic import TemplateView

class AboutPageView(TemplateView):
    template_name = 'about.html'
    
class HomePageView(TemplateView):
    template_name = 'home.html'

