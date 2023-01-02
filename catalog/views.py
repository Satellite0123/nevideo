from django.shortcuts import render
from django.views.generic import TemplateView
from . import models

# Create your views here.

class MainView(TemplateView):
    template_name = "catalog/main.html"
    
    def get_context_data(self, **kwargs):
        print("GAGFAGD")
        context = super(MainView, self).get_context_data(**kwargs)
        
        categories = models.Category.objects

        context['categories'] = categories
        print("CATEG", categories)
        return context
