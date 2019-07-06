from django.shortcuts import redirect
from django.urls import reverse

def main_redir(request):
	return redirect('blog_posts_url')