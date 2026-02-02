from django.shortcuts import render,get_object_or_404
from datetime import date
from .models import Post,Author,Tag
from django.views.generic import ListView,DetailView
from .forms import CommentForm

# Create your views here.

all_posts = [
]

def get_date(post):
    return post['date']

class StartingPageView(ListView):
    model=Post
    template_name="blog/index.html"
    context_object_name="posts"
    ordering=["-date"]

    def get_queryset(self):
        queryset=super().get_queryset()
        top3posts=queryset[:3]
        return top3posts
    

# def posts(request):
#     all_posts=Post.objects.all().order_by("-date")
#     return render(request,"blog/all_posts.html",{"all_posts":all_posts})

class PostsView(ListView):
    model=Post
    template_name="blog/all_posts.html"
    context_object_name="all_posts"
    ordering=["-date"]


class SinglePostView(DetailView):
    model=Post
    template_name="blog/post_detail.html"
    context_object_name="post"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post_tags"] = self.object.tags.all()
        context["comment_form"]=CommentForm()
        return context
    

chrome://settings/clearBrowserData

# def posts_detail(request,slug):
#     # specific_post=Post.objects.get(slug=slug)       
#     specific_post=get_object_or_404(Post,slug=slug)                    
#     return render(request,"blog/post_detail.html",{"post":specific_post,"tags":specific_post.tags.all()})


# def posts_detail(request, slug):
#     specific_post = get_object_or_404(Post, slug=slug)
#     return render(request, "blog/post_detail.html", {
#         "post": specific_post,
#         "tags": specific_post.tags.all()
#     })