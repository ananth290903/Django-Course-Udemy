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

    def is_post_selected(self,request,post_id):
        stored_posts=request.session.get("read_later_posts")
        if(stored_posts is not None):
            specific_post_id=post_id
            read_later_for_post=int(specific_post_id) in stored_posts
        else:
            read_later_for_post=False

        return read_later_for_post
 
    def get(self,request,slug):
        post=Post.objects.get(slug=slug)
        comments=post.comments.all()
        read_later_for_post=self.is_post_selected(request,post.id)
        context={"post":post,"post_tags":post.tags.all(),"comment_form":CommentForm(),"comments":comments.order_by("-id"),
                 "read_later_for_post":read_later_for_post}
        return render(request,"blog/post_detail.html",context)

    def post(self,request,slug):
        comment_form=CommentForm(request.POST)
        post=Post.objects.get(slug=slug)
        read_later_for_post=self.is_post_selected(request,post.id)
        comments=post.comments.all()
        if(comment_form.is_valid()):
            comment=comment_form.save(commit=False)
            comment.post=post
            comment.save()
            return HttpResponseRedirect(reverse('post-detail-page',args=[slug]))
        
        context={
            'post':post,
            'post_tags':Post.tags.get(slug=slug).tags.all(),
            'comment_form':comment_form,
            "comments":  comments.order_by("-id"),
            "read_later_for_post":read_later_for_post
        }
        
        return render(request,"blog/post_detail.html",context)
  
class ReadLaterView(View):
    def get(self,request):
        context={}
        stored_posts=request.session.get('read_later_posts')
        if(stored_posts is None or len(stored_posts)==0):
            context['any_posts_selected']=False
            context['posts']=[]
        else:
            context['any_posts_selected']=True
            context['posts']=Post.objects.filter(id__in=stored_posts)

        return render(request,"blog/stored_posts.html",context)


    def post(self,request):
        stored_posts=request.session.get('read_later_posts')
        post_id=int(request.POST['post_id'])
        if(stored_posts is None):
            stored_posts=[]
        if(post_id not in stored_posts):
            stored_posts.append(post_id)
        else:
             stored_posts.remove(post_id)
        request.session['read_later_posts']=stored_posts
        return HttpResponseRedirect(reverse('starting-page'))
    
        






    


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