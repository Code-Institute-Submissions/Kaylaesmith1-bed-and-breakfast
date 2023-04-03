from django.shortcuts import render, get_list_or_404
from django.views import generic, View
from .forms import CustomerForm
# from django.core.mail import send_mail, BadHeaderError
# from django.http import HttpResponse


class Home(generic.TemplateView):
    """Opens to landing page"""
    template_name = "index.html"


# class Contact(generic.TemplateView):
#     """Opens to Contact Us page"""

#     template_name = "contact_us.html"
    
#     def get(self, request):
#         form = CustomerForm()

#         return render(request, "contact_us.html", {'form': form})

    


class About(generic.TemplateView):
    """Opens About page"""
    template_name = "about.html"


def create_customer(request):
    form = CustomerForm()
    return render(request, 'contact_us.html', {'form': form})

# POST A REVIEW OF THE BNB - from Django blog walkthrough?
# class PostDetail(View):

#     def get(self, request, slug, *args, **kwargs):
#         queryset = Post.objects.filter(status=1)
#         review = get_object_or404(queryset, slug=slug).order_by('created_on')
#         liked = False
#         if post.likes.filter(id=self.request.user.id).exists():
#             liked = True

#         return render (
#             request,
#             "about.html",
#             {
#                 "review": review,
#                 "liked": liked
#             },
#         )
