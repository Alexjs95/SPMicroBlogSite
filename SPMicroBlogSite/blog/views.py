from django.shortcuts import render
from blog.models import Post, Comment
from .forms import CommentForm
from snowplow_tracker import Tracker, Emitter, Subject

e = Emitter("d3rkrsqld9gmqf.cloudfront.net")
s = Subject().set_user_id("AJS").set_lang("eng")    # track main user
t = Tracker(e)
    
def index_blog(request):
    posts = Post.objects.all().order_by("-created_on")
    context = {"posts": posts}
    
    t.track_page_view("localhost:8000/blog", "index")   # page view track

    return render(request, "index_blog.html", context)


def blog_category(request, category):
    posts = Post.objects.filter(categories__name__contains=category).order_by(
        "-created_on"
    )
    context = {"category": category, "posts": posts}
    
    t.track_page_view("localhost:8000/blog/$category", "blog category") # page view track
    
    return render(request, "blog_category.html", context)


def blog_post(request, pk):
    post = Post.objects.get(pk=pk)
    comments = Comment.objects.filter(post=post)
    t.track_page_view("localhost:8000/blog/$id", "blog post view") # page view track
    
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author = form.cleaned_data["author"],
                body = form.cleaned_data["body"],
                post = post,
            )
            comment.save()
            t.track_form_submit("CommentForm")      # Track that commentform been submitted

    context = {"post": post, "comments": comments, "form": form}
    return render(request, "blog_post.html", context)