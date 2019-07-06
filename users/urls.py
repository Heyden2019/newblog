from django.urls import path, include
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('signin/', views.signin, name='signin'),
    path('logout/', views.logout_view, name='logout'),
    path('password_change', views.password_change, name='password_change'),
    path('password_reset/', views.PasswordReset.as_view(), name='password_reset'),
	path('password_reset/done/', views.PasswordResetDone.as_view(), name='password_reset_done'),
	path('reset/<uidb64>/<token>/', views.PasswordResetConfirm.as_view(), name='password_reset_confirm'),
	path('reset/done/', views.PasswordResetComplete.as_view(), name='password_reset_complete'),
	]
