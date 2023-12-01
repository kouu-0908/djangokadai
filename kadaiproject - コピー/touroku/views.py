from django.shortcuts import render
from django.views.generic.base import TemplateView
 
class TourokuView(TemplateView):
    template_name = 'touroku.html'
