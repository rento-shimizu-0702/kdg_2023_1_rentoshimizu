from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Shioriha_Profile

# Create your views here.
class HomeView(ListView):
    template_name = 'infomation/index.html'
    model = Shioriha_Profile

class ProfileView(ListView):
    template_name = 'infomation/profile.html'
    model = Shioriha_Profile

class StreamingView(ListView):
    template_name = 'infomation/streaming.html'
    model = Shioriha_Profile

class LinkView(ListView):
    template_name = 'infomation/link.html'
    model = Shioriha_Profile
