from django.shortcuts import render
from django.urls import reverse
from .forms import ReviewForm
from django.http import HttpResponseRedirect
from .models import Review


def review(request):
    if(request.method=="POST"):
        print("The request is",request)
        record=Review.objects.get(id=3)
        form=ReviewForm(request.POST,record)
        if(form.is_valid()):
            form.save()
            redirect_url=reverse("thank_you_url",args=[])
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