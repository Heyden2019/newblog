from django import forms
from .models import *
from time import time
from django.core.exceptions import ValidationError
from django.utils.text import slugify


class TagForm(forms.ModelForm):

	obj_id = None
	#using when edit

	class Meta:
		model = Tags
		fields = ['title']
		widgets = {
			'title': forms.TextInput(attrs={'class': 'form-control'}),
		}
		labels = {
			'title': 'Enter title',
		}
	
	def clean_title(self):
		new_title = self.cleaned_data['title'].lower()
		n_slug = slugify(new_title)
		filt_slug = self.Meta.model.objects.filter(slug__iexact=n_slug)
		if n_slug == 'create':
			raise ValidationError('You shall not create this title #1"create"')
		if filt_slug:
			if self.obj_id:
				if self.obj_id != filt_slug[0].id:
					raise ValidationError('You shall not edit this title like you do #4"Unique"')
			else:
				raise ValidationError('You shall not create this title #2"Unique"')
		if not n_slug:
			raise ValidationError('You shall not create this title #3"Empty"')
		return new_title
		
class PostForm(forms.ModelForm):

	obj_id = None
	#using when edit

	class Meta:
		model = Posts
		fields = ['title', 'body', 'tags']
		widgets = {
			'title': forms.TextInput(attrs={'class': 'form-control'}),
			'body': forms.Textarea(attrs={'class': 'form-control', 'style': 'height: 250px; resize: none;'}),
			'tags': forms.CheckboxSelectMultiple(attrs={'class': 'form-check'}),
		}

		labels = {
			'title': 'Enter "title":',
			'body': 'Enter text:',
			'tags': 'Choose tags',
		}

	def clean_title(self):
		new_title = self.cleaned_data['title'].lower()
		n_slug = slugify(new_title)
		filt_slug = self.Meta.model.objects.filter(slug__iexact=n_slug)
		if n_slug == 'create':
			raise ValidationError('You shall not create this title #1"create"')
		if filt_slug:
			if self.obj_id:
				if self.obj_id != filt_slug[0].id:
					raise ValidationError('You shall not edit this title like you do #4"Unique"')
			else:
				raise ValidationError('You shall not create this title #2"Unique"')
		if not n_slug:
			raise ValidationError('You shall not create this title #3"Empty"')
		return new_title


class CommentForm(forms.ModelForm):
	class Meta:
		model = Comments
		fields = ['comment']
		widgets = {'comment': forms.Textarea(attrs={'class': 'form-control', 'style': 'height: 70px; resize: none;'})}
		labels = {'comment': 'Enter your comment:'}