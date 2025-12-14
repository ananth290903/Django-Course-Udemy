from django.shortcuts import render
from django.urls import reverse
from .forms import ReviewForm
from django.http import HttpResponseRedirect
from .models import Review



def review(request):
    if(request.method=="POST"):
        form=ReviewForm(request.POST)
        if(form.is_valid()):
            review=Review(user_name=form.cleaned_data['user_name'],
                          rating=form.cleaned_data['rating'],
                          review_text=form.cleaned_data['review_text'])
            review.save()
            redirect_url=reverse('thank_you_url',args=[])
            return HttpResponseRedirect(redirect_url)

    else:
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