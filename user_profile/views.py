from django.shortcuts import render

from django.contrib.auth.decorators import login_required

from user_auth.models import User
from user_profile.forms import UserProfileForm
from user_profile.models import UserProfile

@login_required
def user_profile_dashboard(request):

	current_user = request.user
	current_user_instance = UserProfile.objects.get(user=current_user) 
	if request.method=="POST":
		form = UserProfileForm(request.POST, instance=current_user_instance, user=current_user)
		if form.is_valid():
			form.save()
	else:
		form = UserProfileForm(user=current_user)
	return render(request, 'user_auth/login_signup.html', {'form': form,
															'user': current_user,})


