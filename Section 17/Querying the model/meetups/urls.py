from django.urls import path,reverse
from . import views

urlpatterns=[
    path('meetups/',views.index,name="meetups"),
    path('meetups/<slug:meetup_slug>/',views.meetup_detail,name="meetup-detail")
]


