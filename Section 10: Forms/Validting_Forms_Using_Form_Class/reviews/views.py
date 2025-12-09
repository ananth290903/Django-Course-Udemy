from django.shortcuts import render 
from django.urls import reverse 
from django.http import HttpResponseRedirect
from .forms import ReviewForm


def review(request):
    if(request.method=="POST"):
        form=ReviewForm(request.POST)
        if(form.is_valid()):
            print(form.cleaned_data)
            redirect_url=reverse("thank_you_url",args=[])
            return HttpResponseRedirect(redirect_url)
        
    form=ReviewForm()
    return render(request,"reviews/review.html",{"form":form})


def thank_you(request):
    return render(request,"reviews/thank_you.html",{})






















# from django.shortcuts import render 
# from django.urls import reverse 
# from django.http import HttpResponseRedirect
# from .forms import ReviewForm


# def review(request):
#     if(request.method=="POST"):
#         username=request.POST["username"]
#         if(username==""):
#             return render(request,"reviews/review.html",{"username_empty":True})
#         print(username)
#         redirect_url=reverse("thank_you_url",args=[])
#         return HttpResponseRedirect(redirect_url)
    
#     return render(request,"reviews/review.html",{"username_empty":False})


# def thank_you(request):
#     return render(request,"reviews/thank_you.html",{})