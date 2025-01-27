from datetime import date

from django.shortcuts import render,get_object_or_404
from .models import Post
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView,DetailView
from django.views.generic.edit import FormView
from .models import Post
from .forms import CommentForm

all_posts = [
]

def get_date(post):
  return post['date']

# Create your views here.



class starting_pageView(ListView):
    model = Post
    template_name = "blog/index.html"
    ordering = ["-date"]
    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset[:3]
        return data
    context_object_name = "posts"    
    

# def starting_page(request):
#     latest_posts = Post.objects.all().order_by("-date")[:3]
#     return render(request, "blog/index.html", {
#       "posts": latest_posts
#     })



class postsView(ListView):
    model = Post
    template_name = "blog/all-posts.html"
    context_object_name = "all_posts"


# def posts(request):
#     all_posts = Post.objects.all()
#     return render(request, "blog/all-posts.html", {
#       "all_posts": all_posts
#     })




class post_detailView(DetailView):
    model = Post
    template_name = "blog/post-detail.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post_tags"] = self.object.tags.all()
        context["comment_form"] = CommentForm()
        return context
    
    
    
    

# def post_detail(request, slug):
#     identified_post = get_object_or_404(Post,slug=slug)
#     return render(request, "blog/post-detail.html", {
#       "post": identified_post,
#       "post_tags" : identified_post.tags.all()
#     })