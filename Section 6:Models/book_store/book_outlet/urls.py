from django.urls import path
from . import views

urlpatterns=[
    path("",views.index),
    path("<slug:slug>",views.book_in_detail,name="book_in_detail")
]
