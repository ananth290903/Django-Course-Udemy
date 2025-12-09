from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect

# Create your views here.
def review(request):
    if(request.method=="POST"):
        username=request.POST['username']
        print(username)
        redirect_url=reverse('thank_you_url')
        return HttpResponseRedirect(redirect_url)
    return render(request,"reviews/review.html",{})

def thank_you(request):
    return render(request,"reviews/thank_you.html",{})