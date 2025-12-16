from django.shortcuts import render
from django.urls import reverse
from .forms import ReviewForm
from django.http import HttpResponseRedirect
from django.views import View
from .models import Review
from django.views.generic.base import TemplateView

class ReviewView(View):
    def get(self,request):
        form=ReviewForm()
        return render(request,"reviews/review.html",{"form":form})

    def post(self,request):
        form=ReviewForm(request.POST)
        if(form.is_valid()):
            form.save()
            redirect_url=reverse('thank_you_url',args=[])
            return HttpResponseRedirect(redirect_url)
        
        return render(request,"review/reviews.html",{"form":form})



class ThankYouView(TemplateView):
    template_name="reviews/thank_you.html"

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['message']="This is a new Work !"
        return context

class ReviewsListViews(TemplateView):
    template_name="reviews/review_list.html"
    def get_context_data(self, **kwargs):
        reviews=Review.objects.all()
        context=super().get_context_data(**kwargs)
        context['reviews']=reviews
        return context























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