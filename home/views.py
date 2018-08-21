from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect, render


def home(request):
	user = request.user
	if user.is_authenticated:

		return render(request, 'home/base.html', {'user': user,})

	else:
		return redirect('../users/login')	


# #logs the user in using the navigation bar at the top
# 	login_form = LoginForm(request.POST)
# 	error_message = ''
# 	if login_form.is_valid():
# 		email = login_form.cleaned_data.get('email')
# 		password = login_form.cleaned_data.get('password')
# 		user = authenticate(request, email=email, password=password)
# 		if user is not None:
# 			login(request, user)
# 		else:
# 			error_message = 'Your email or password did not match'
# 	else:
# 		login_form = LoginForm()

# 	return render(request, 'home/base.html', {	'user': user,
# 												'login_form': login_form,})

