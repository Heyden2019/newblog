from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.exceptions import ValidationError
from .models import *
from django.urls import reverse
from django.views.generic import View
from .utils import *
from .forms import *
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.decorators import login_required

class blogPosts(BlogObjectsMixin, View):
	model = Posts
	url = 'blog/blog.html'
	paginator = True
		
class blogTags(BlogObjectsMixin, View):
	model = Tags
	url = 'blog/tags.html'

class blogPost(View):
	#BlogObjectMixin
	model = Posts
	url = 'blog/post.html'

	def get(self, request, slug):
		obj = get_object_or_404(self.model, slug__iexact=slug)
		form = CommentForm()
		comments = Comments.objects.filter(post=obj.id)
		context = {
			'posts': obj,
			'admin_option': obj,
			'form': form,
			'comments': comments,
		}
		return render(request, self.url, context=context)

	#@login_required()
	def post(self, request, slug):
		if not request.user.is_authenticated:
			raise ValidationError('You can\'t commenting')
		obj = get_object_or_404(self.model, slug__iexact=slug)
		bound_form = CommentForm(request.POST)
		if bound_form.is_valid():
			new_comment = bound_form.save(commit=False)
			print('111111111111111111111111111111111111')
			new_comment.author = request.user
			new_comment.post = obj
			new_comment.save()
			return HttpResponseRedirect(reverse('blog_post_url', args=[slug]))
			#bound_form = CommentForm()
		comments = Comments.objects.filter(post=obj.id)
		context = {
			'posts': obj,
			'admin_option': obj,
			'form': bound_form,
			'comments': comments,
		}
		return render(request, self.url, context=context)




class blogTag(BlogObjectMixin, View):
	model = Tags
	url = 'blog/tag.html'
	paginator = True
	
class CreateTag(PermissionRequiredMixin, CreateObjectMixin, View):
	permission_required = 'blog.add_tags'
	form_model = TagForm
	url_main = 'blog/create_tag.html'
	url_for_redir = 'blog_tag_url'
	
class CreatePost(PermissionRequiredMixin, CreateObjectMixin, View):
	permission_required = 'blog.add_posts'
	form_model = PostForm
	url_main = 'blog/create_post.html'
	url_for_redir = 'blog_post_url'

class EditTag(PermissionRequiredMixin, EditObjMixin, View):
	permission_required = 'blog.change_tags'
	form_model = TagForm
	url_main = 'blog/edit_tag.html'
	url_for_redir = 'blog_tag_url'

class EditPost(PermissionRequiredMixin, EditObjMixin, View):
	permission_required = 'blog.change_posts'
	form_model = PostForm
	url_main = 'blog/edit_post.html'
	url_for_redir = 'blog_post_url'

class DelTag(PermissionRequiredMixin, DelObjectMixin, View):
	permission_required = 'blog.delete_tags'
	model = Tags
	url_main = 'blog/del_obj.html'

class DelPost(PermissionRequiredMixin, DelObjectMixin, View):
	permission_required = 'blog.delete_posts'
	model = Posts
	url_main = 'blog/del_obj.html'





