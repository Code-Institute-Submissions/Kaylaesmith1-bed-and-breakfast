from django.shortcuts import render
from django.views import generic, View
# from .forms import ContactForm
# from django.core.mail import send_mail, BadHeaderError
# from django.http import HttpResponse


class Home(generic.TemplateView):
    """Opens to landing page"""
    template_name = "index.html"


class Contact(generic.TemplateView):
    """Opens to Contact Us page"""
    template_name = "contact_us.html"


class About(generic.TemplateView):
    """Opens About page"""
    template_name = "about.html"
