from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path, re_path

from . import views

urlpatterns = [
	path('profile/', views.user_profile_dashboard, name='profile'),
]
