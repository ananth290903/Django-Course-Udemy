from . import views
from django.urls import path

urlpatterns=[
    path("",views.ReviewView.as_view(),name="review"),
    path("thank_you",views.ThankYouView.as_view(),name="thank_you_url"),
    path("reviews",views.ReviewsListViews.as_view()),
    path("reviews/<int:pk>",views.SingleReviewView.as_view())
]