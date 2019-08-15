from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import *
from django.core.paginator import Paginator
from django.db.models import Q
from django.core.exceptions import ValidationError


class BlogObjectsMixin:
	model = None
	url = None
	paginator = False
	context = {}

	def get(self, request):
		search = request.GET.get('searcher', '')
		if search:
			objects = self.model.objects.filter(Q(title__icontains=search) | Q(body__icontains=search))
		else:
			objects = self.model.objects.all()
		if self.paginator:
			pagin = Paginator(objects, 6)
			page = request.GET.get('page', '1')
			if int(page) not in pagin.page_range:
				page = 1
			objects = pagin.get_page(page)
			self.context['pagin'] = pagin
		self.context[self.model.__name__.lower()] = objects 
		return render(request, self.url, context=self.context)

class BlogObjectMixin:
	model = None
	url = None
	paginator = False
	context = {}

	def get(self, request, slug):
		obj = get_object_or_404(self.model, slug__iexact=slug)
		if self.paginator:
			objects = obj.posts.all()
			pagin = Paginator(objects, 2)
			page = request.GET.get('page', '1')
			if int(page) not in pagin.page_range:
				page = 1
			objects = pagin.get_page(page)
			self.context = {
				'pagin': pagin,
				'objects': objects,
			}
		self.context.update({
			self.model.__name__.lower(): obj,
			'admin_option': obj,
		})
		return render(request, self.url, context=self.context)

class CreateObjectMixin:
	form_model = None 
	url_main = None
	url_for_redir = None

	def get(self, request):
		form = self.form_model()
		return render(request, self.url_main, {'form': form})

	def post(self, request):
		bound_form = self.form_model(request.POST)
		if bound_form.is_valid():
			new = bound_form.save(commit=False)
			new.autor = request.user
			new.save()
			two = bound_form.save_m2m()
			print(two)
			return redirect(self.url_for_redir, new.slug)
		return render(request, self.url_main, {'form': bound_form})

class EditObjMixin:
	form_model = None
	url_main = None
	url_for_redir = None
	def get(self, request, slug):
		obj = get_object_or_404(self.form_model.Meta.model, slug__iexact=slug)
		form = self.form_model(instance=obj)
		return render(request, self.url_main, {'form': form, 'obj': obj})
	def post(self, request, slug):
		obj = get_object_or_404(self.form_model.Meta.model, slug__iexact=slug)
		self.form_model.obj_id = obj.id
		print(obj.id)
		bound_form = self.form_model(request.POST, instance=obj)
		if bound_form.is_valid():
			new_obj = bound_form.save()
			return redirect(self.url_for_redir, new_obj.slug)
		return render(request, self.url_main, {'form': bound_form})

class DelObjectMixin:
	model = None 
	url_main = None

	def get(self, request, slug):
		obj = get_object_or_404(self.model, slug__iexact=slug)
		return render(request, self.url_main, {'obj': obj})

	def post(self, request, slug):
		obj = get_object_or_404(self.model, slug__iexact=slug)
		obj.delete()
		if self.model.__name__ == 'Posts':
			return redirect('blog_posts_url')
		return redirect('blog_tags_url')