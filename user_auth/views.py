from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render

from user_auth.forms import LoginForm, UserCreationForm

def signup(request):
	form_type = 'Sign Up'
	if request.method=="POST":
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			email = form.cleaned_data.get('email')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(email=email, password=raw_password)
			login(request, user)
			return redirect('../../profile/setup')
	else:
		form = UserCreationForm()
	return render(request, 'users/login.html', {'form': form,
												'form_type': form_type,
		})

def user_login(request):
	form_type = 'Login'
	form = LoginForm(request.POST)
	error_message = ''
	if form.is_valid():
		email = form.cleaned_data.get('email')
		password = form.cleaned_data.get('password')
		user = authenticate(request, email=email, password=password)
		if user is not None:
			login(request, user) #need to redirect to some other view of the site
			return redirect('../../')			
		else:
			error_message = 'Invalid email or password'
	else:
		form = LoginForm()
	return render(request, 'users/login.html', {'form': form,
												'form_type': form_type,
												'error_message': error_message,})

def user_logout(request):
	logout(request)
	return redirect('../login')
