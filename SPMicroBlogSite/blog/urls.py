from django.urls import path
from . import views

urlpatterns = [
    path("", views.index_blog, name="index_blog"),
    path("<int:pk>/", views.blog_post, name="blog_post"),
    path("<category>/", views.blog_category, name="blog_category"),
]