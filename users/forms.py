from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.core.exceptions import ValidationError

class UserCreationForm_new(UserCreationForm):
	email = forms.EmailField(label='Email')
	
	class Meta:
		model = User
		fields = ('username', 'email', 'password1', 'password2')

	def clean_email(self):
		email = self.cleaned_data['email'].lower()
		if self.Meta.model.objects.filter(email__iexact=email):
			raise ValidationError('email must be Unique')
		else:
			return email
