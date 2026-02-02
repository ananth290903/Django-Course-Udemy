from . import views
from django.urls import path

urlpatterns=[
    path("",views.StartingPageView.as_view(),name="starting-page"),
    path("posts",views.PostsView.as_view(),name="posts-page"),
    path("posts/<slug:slug>",views.SinglePostView.as_view(),name="post-detail-page"),
    path("read-later",views.ReadLaterView.as_view(),name="read-later")
]