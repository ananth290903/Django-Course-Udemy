from django.shortcuts import render,get_object_or_404
from datetime import date
from .models import Post,Author,Tag
from django.views.generic import ListView,DetailView
from .forms import CommentForm
from django.views import View
from django.http import HttpResponseRedirect
from django.urls import reverse

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


class SinglePostView(View):
    # model=Post
    # template_name="blog/post_detail.html"
    # context_object_name="post"


    def get(self,request,slug):
        post=Post.objects.get(slug=slug)
        comments=post.comments.all()
        context={"post":post,"post_tags":post.tags.all(),"comment_form":CommentForm(),"comments":comments.order_by("-id")}
        return render(request,"blog/post_detail.html",context)

    def post(self,request,slug):
        comment_form=CommentForm(request.POST)
        post=Post.objects.get(slug=slug)
        comments=post.comments.all()
        if(comment_form.is_valid()):
            comment=comment_form.save(commit=False)
            comment.post=post
            comment.save()
            return HttpResponseRedirect(reverse('post-detail-page',args=[slug]))
        
        context={
            'post':Post,
            'post_tags':Post.tags.get(slug=slug).tags.all(),
            'comment_form':comment_form,
            "comments":  comments.order_by("-id")
        }
        
        return render(request,"blog/post_detail.html",context)
  
class ReadLaterView(View):
    def get(self,request):
        context={}
        stored_posts=request.session.get('read_later_posts',[])
        if(len(stored_posts)!=0):
            any_posts_selected=True
            context['any_posts_selected']=any_posts_selected
            stored_post_objects=Post.objects.filter(id__in=stored_posts)
            context['posts']=stored_post_objects

        else:
            any_posts_selected=False
            context['any_posts_selected']=any_posts_selected
            context['posts']=[]

        return render(request,"blog/stored_posts.html",context)


    def post(self,request):
        post_id=request.POST.get('post_id')
        if(post_id is not None):
            existing_list_posts=request.session.get('read_later_posts',[])
            if(post_id not in existing_list_posts):
                existing_list_posts.append(int(post_id))
                request.session['read_later_posts']=existing_list_posts
                return HttpResponseRedirect(reverse('read-later'))
    


    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["post_tags"] = self.object.tags.all()
    #     context["comment_form"]=CommentForm()
    #     return context
    



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