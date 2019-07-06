from django.urls import path
from .views import *

urlpatterns = [
    path('', blogPosts.as_view(), name = 'blog_posts_url'),
    path('post/create/', CreatePost.as_view(), name = 'blog_create_post_url'),
    path('post/<slug:slug>/', blogPost.as_view(), name = 'blog_post_url'),
    path('post/<slug:slug>/edit/', EditPost.as_view(), name = 'blog_post_edit_url'),
    path('post/<slug:slug>/del/', DelPost.as_view(), name = 'blog_post_del_url'),
    path('tags/', blogTags.as_view(), name = 'blog_tags_url'),
    path('tag/create/', CreateTag.as_view(), name = 'blog_tag_create_url'),
    path('tag/<slug:slug>/', blogTag.as_view(), name = 'blog_tag_url'),
    path('tag/<slug:slug>/edit/', EditTag.as_view(), name = 'blog_tag_edit_url'),
    path('tag/<slug:slug>/del/', DelTag.as_view(), name = 'blog_tag_del_url'),
]
