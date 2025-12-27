from django.shortcuts import render
from django.urls import path,reverse,reverse_lazy
from django.http import HttpResponseRedirect
from django.views import View
from .forms import ProfileForm
from .models import UserProfile
from django.views.generic.edit import CreateView
from django.views.generic import ListView


class CreateProfileView(CreateView):
    template_name="profiles/create_profile.html"
    model=UserProfile
    fields="__all__"
    success_url=reverse_lazy("profiles")


class ProfilesView(ListView):
    model=UserProfile
    template_name="profiles/user_profiles.html"
    context_object_name="profiles"





































# from django.shortcuts import render
# from django.views import View
# from django.http import HttpResponseRedirect

# # Create your views here.

# def store_file(file):
#     with open("temp/image.jpg", "wb+") as dest:
#         for chunk in file.chunks():
#             dest.write(chunk)


# class CreateProfileView(View):
#     def get(self, request):
#         return render(request, "profiles/create_profile.html")

#     def post(self, request):
#         store_file(request.FILES["image"])
#         return HttpResponseRedirect("/profiles")

