from django.shortcuts import render, get_list_or_404
from django.views import generic, View
from .forms import CustomerForm
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect


class Home(generic.TemplateView):
    """Opens to landing page"""
    template_name = "index.html"


class About(generic.TemplateView):
    """Opens About page"""
    template_name = "about.html"


def create_customer(request):
    form = CustomerForm()
    return render(request, 'contact_us.html', {'form': form})


# def contactView(request):
#     if request.method == "GET":
#         form = CustomerForm()
#     else:
#         form = CustomerForm(request.POST)
#         if form.is_valid():
#             subject = form.cleaned_data["subject"]
#             from_email = form.cleaned_data["from_email"]
#             message = form.cleaned_data['message']
#             try:
#                 send_mail(subject, message, from_email, ["kaylaesmith1@gmail.com"])
#             except BadHeaderError:
#                 return HttpResponse("Invalid header found.")
#             return redirect("success")
#     return render(request, 'contact_us.html', {'form': form})

# def successView(request):
#     return HttpResponse("Success! Thank you for your message.")

    
