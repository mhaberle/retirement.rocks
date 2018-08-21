from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render

from user_auth.forms import LoginForm, UserCreationForm

def user_signup(request, sign_up_type):
	form_title = 'Sign Up'
	login_link = ''
	error_message = ''
	if sign_up_type == 'freelance':
		user_type = 'freelancer'
	else:
		user_type = 'employer'

	if request.method=="POST":
		form = UserCreationForm(request.POST, user_type=user_type)
		if form.is_valid():
			form.save()
			email = form.cleaned_data.get('email')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(email=email, password=raw_password)
			login(request, user)
			return redirect('../../profile/setup')#need to update
	else:
		form = UserCreationForm(user_type=user_type)
	return render(request, 'user_auth/login_signup.html', { 'form': form,
															'form_title': form_title,
															'login_link': login_link,
															'error_message': error_message,
		})

def user_login(request):
	form_title = 'Login'
	signup_link = ''
	error_message = ''


	form = LoginForm(request.POST)
	error_message = ''


	if form.is_valid():
		email = form.cleaned_data.get('email')
		password = form.cleaned_data.get('password')
		user = authenticate(request, email=email, password=password)
		if user is not None:
			login(request, user)
			return redirect('../../')#need to update		
		else:
			error_message = 'Invalid email or password'
	else:
		form = LoginForm()
	return render(request, 'user_auth/login_signup.html', {	'form': form,
															'form_title': form_title,
															'signup_link': signup_link,
															'error_message': error_message,
		})

def user_logout(request):
	logout(request)
	return redirect('../login')
