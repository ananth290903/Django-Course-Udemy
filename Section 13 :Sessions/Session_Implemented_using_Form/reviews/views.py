from reviews.models import Review
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView

from .forms import ReviewForm
from .models import Review
from django.urls import path,reverse

# Create your views here.


class ReviewView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = "reviews/review.html"
    success_url = "/thank-you"


class ThankYouView(TemplateView):
    template_name = "reviews/thank_you.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = "This works!"
        return context


class ReviewsListView(ListView):
    template_name = "reviews/review_list.html"
    model = Review
    context_object_name = "reviews"

    # def get_queryset(self):
    #     base_query = super().get_queryset()
    #     data = base_query.filter(rating__gt=4)
    #     return data


class SingleReviewView(DetailView):
    template_name = "reviews/single_review.html"
    model = Review

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        loaded_review=self.object
        fav_review_id=self.request.session.get("fav_review")
        if(fav_review_id is not None):
            is_favourite_review=int(fav_review_id)==loaded_review.id
        print("The fav_review_id is",fav_review_id)
        context['is_favourite_review']=is_favourite_review
        return context
    

class FavouriteReviewView(View):
    def post(self,request):
        review_id=request.POST["review_id"]
        request.session['fav_review']=review_id
        print("The fav review of the user is",review_id)
        redirect_url=reverse("review_by_id",args=[review_id])
        return HttpResponseRedirect(redirect_url)




