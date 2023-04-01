from django.shortcuts import render, reverse
from django.views import generic, View


class Home(generic.TemplateView):
    """Opens to landing page"""
    template_name = "index.html"

class Contact(generic.TemplateView):
    """Opens to Contact Us page"""
    template_name = "contact_us.html"

# class About(generic.TemplateView):
#     """Opens to Contact Us page"""
#     template_name = "about.html"
