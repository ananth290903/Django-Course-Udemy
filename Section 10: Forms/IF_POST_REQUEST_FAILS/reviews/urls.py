from . import views
from django.urls import path

urlpatterns=[
    path("",views.review),
    path("thank-you",views.thank_you,name="thank_you_url")
]