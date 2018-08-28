from django.contrib.auth import authenticate, login, logout
from django.http import Http404
from django.shortcuts import redirect, render

from user_auth.forms import LoginForm, UserCreationForm

def user_signup(request, sign_up_type='not_specified'):
	form_title = 'Sign Up'
	login_link = '' #corresponds to a link if someone wants to login
	opposite_link = ''
	opposite_link_message = ''
	error_message = ''

	#signals what type of user profile to create
	if sign_up_type == 'freelance':
		user_type = 'freelancer'
	elif sign_up_type == 'post-an-opportunity':
		user_type = 'employer'
	else:
		sign_up_type = 'not_specified'

	#set the variable to get the user to alternate signup page if they clicked on the wrong one
	if sign_up_type == "freelance":
		opposite_link = "post-an-opportunity"
		opposite_link_message = "post an opportunity"
	else:
		opposite_link  = "freelance"
		opposite_link_message = "freelance or volunteer"

	if user_type != 'not_specified':
		if request.method=="POST":
			form = UserCreationForm(request.POST, user_type=user_type)
			if form.is_valid():
				form.save()
				email = form.cleaned_data.get('email')
				raw_password = form.cleaned_data.get('password1')
				user = authenticate(email=email, password=raw_password)
				login(request, user)
				return redirect('../../profile/setup')#redirect to user profile
		else:
			form = UserCreationForm(user_type=user_type)
	else:
		raise Http404("That page does not exist")
	return render(request, 'user_auth/login_signup.html', { 'form': form,
															'form_title': form_title,
															'login_link': login_link,
															'opposite_link': opposite_link,
															'opposite_link_message': opposite_link_message,
															'error_message': error_message,
															})

def user_login(request):
	form_title = 'Log In'
	signup_link = '' #corresponds to a link if someone wants to signup
	error_message = ''

	form = LoginForm(request.POST)
	if form.is_valid():
		email = form.cleaned_data.get('email')
		password = form.cleaned_data.get('password')
		user = authenticate(request, email=email, password=password)
		if user is not None:
			login(request, user)
			return redirect('../../')#redirect to user profile		
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

