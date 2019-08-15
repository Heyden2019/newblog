from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.urls import reverse
from django.contrib.auth.models import User

def gen_slug(title):
	slugy = slugify(title)
	return slugy


class Posts(models.Model):
	autor = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length=50, unique=True)
	slug = models.SlugField(max_length=100, unique=True)
	body = models.TextField(max_length=255)
	create_date = models.DateTimeField(default=timezone.now)
	tags = models.ManyToManyField('Tags', blank=True, related_name='posts')

	class Meta:
		ordering = ['-create_date']

	def get_main_url(self):
		return reverse('blog_post_url', kwargs = {'slug': self.slug})

	def get_edit_url(self):
		return reverse('blog_post_edit_url', kwargs = {'slug': self.slug})

	def get_del_url(self):
		return reverse('blog_post_del_url', kwargs = {'slug': self.slug})

	def __str__(self):
		return self.title

	def save(self, *args, **kwargs):
		#if not self.id:
		self.slug = gen_slug(self.title)
		super().save(*args, **kwargs)

class Tags(models.Model):
	title = models.CharField(max_length=20, unique=True)
	slug = models.SlugField(max_length=20, unique=True) 

	def __str__(self):
		return self.title
		
	def get_main_url(self):
		return reverse('blog_tag_url', kwargs = {'slug': self.slug})

	def get_edit_url(self):
		return reverse('blog_tag_edit_url', kwargs = {'slug': self.slug})

	def get_del_url(self):
		return reverse('blog_tag_del_url', kwargs = {'slug': self.slug})

	def save(self, *args, **kwargs):
		#if not self.id:
		self.slug = gen_slug(self.title)
		super().save(*args, **kwargs)

class Comments(models.Model):
	author = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default=1)
	post = models.ForeignKey(Posts, on_delete=models.CASCADE)
	create_date = models.DateTimeField(default=timezone.now)
	comment = models.TextField(max_length=255)

	class Meta:
		ordering = ['-create_date']

	def __str__(self):
		return  self.comment[0:100]