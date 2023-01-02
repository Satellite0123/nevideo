from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class MainView(TemplateView):
    template_name = "player/main.html"

class WatchView(TemplateView):
    template_name = "player/watch.html"