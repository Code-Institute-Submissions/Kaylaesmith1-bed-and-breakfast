from django.shortcuts import render
from django.views import generic, View


class Home(generic.TemplateView):
    """Opens to landing page"""
    template_name = "index.html"
