from django.shortcuts import render
from django.urls import reverse,reverse_lazy
from .forms import ReviewForm
from django.http import HttpResponseRedirect
from django.views import View
from .models import Review
from django.views.generic.base import TemplateView
from django.views.generic import ListView,DetailView,FormView


# class ReviewView(View):
#     def get(self,request):
#         form=ReviewForm()
#         return render(request,"reviews/review.html",{"form":form})

#     def post(self,request):
#         form=ReviewForm(request.POST)
#         if(form.is_valid()):
#             form.save()
#             redirect_url=reverse('thank_you_url',args=[])
#             return HttpResponseRedirect(redirect_url)
        
#         return render(request,"review/reviews.html",{"form":form})

class ReviewView(FormView):
    form_class=ReviewForm
    template_name="reviews/review.html"
    success_url=reverse_lazy('thank_you_url',args=[])

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)



class ThankYouView(TemplateView):
    template_name="reviews/thank_you.html"

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['message']="This is a new Work !"
        return context
    

class ReviewsListViews(ListView):
    template_name="reviews/review_list.html"
    model=Review
    context_object_name="reviews"

# class ReviewsListViews(ListView):
#     template_name="reviews/review_list.html"
#     model=Review
#     context_object_name="reviews"
    
# class SingleReviewView(TemplateView):
#     template_name="reviews/detailed_review.html"
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         review_id=kwargs["id"]
#         specific_review=Review.objects.get(pk=review_id)
#         context['detailed_post']=specific_review
#         return context


class SingleReviewView(FormView):
    form_class=ReviewForm
    template_name="reviews/detailed_review.html"

    























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