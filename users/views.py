from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from .forms import UserCreationForm_new
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView


def register(request):
	if request.method == 'POST':
		form = UserCreationForm_new(request.POST)
		if form.is_valid() and self.request.recaptcha_is_valid:
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(request, username = username, password  = password)
			login(request, user)
			messages.success(request, 'You create a new user')
			return redirect('blog_posts_url') 
	else:
		form = UserCreationForm_new()
	return render(request, 'users/register.html', {'form': form})

def signin(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username = username, password  = password)
		if user is not None:
			login(request, user)
			return redirect('blog_posts_url')
		else:
			form = AuthenticationForm(request.POST)
			message = 'Incorrect login or password'
			return render(request, 'users/signin.html', {
				'form': form,
				'message': message,
				})
	else:
		form = AuthenticationForm()
	return render(request, 'users/signin.html', {'form': form})

@login_required
def logout_view(request):
	logout(request)
	return redirect('blog_posts_url')

@login_required
def password_change(request):
	if request.method == 'POST':
		form = PasswordChangeForm(user = request.user, data = request.POST)
		if form.is_valid():
			form.save()
			update_session_auth_hash(request, form.user)
			return render(request, 'users/password_change_done.html', {'form': form})
	else:
		form = PasswordChangeForm(user = request.user)
	return render(request, 'users/password_change.html', {'form': form})

class PasswordReset(PasswordResetView):
	template_name = 'users/password_reset.html'
	email_template_name = 'users/password_reset_email.html'


class PasswordResetDone(PasswordResetDoneView):
	template_name = 'users/password_reset_done.html'

class PasswordResetConfirm(PasswordResetConfirmView):
	template_name = 'users/password_reset_confirm.html'

class PasswordResetComplete(PasswordResetCompleteView):
	template_name = 'users/password_reset_complete.html'