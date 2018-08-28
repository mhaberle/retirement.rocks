from django.conf import settings
from django.contrib.auth import get_user_model
from django.forms import ModelForm

from .models import UserProfile
from user_auth.models import User

class UserProfileForm(ModelForm):
	user = None

	def __init__(self, *args, **kwargs):
		self.user = kwargs.pop('user')
		super(UserProfileForm, self).__init__(*args, **kwargs)
		profile_instance = UserProfile.objects.get(user=self.user)

		self.initial['first_name'] = profile_instance.first_name
		self.initial['last_name'] = profile_instance.last_name
		self.initial['birth_date'] = profile_instance.birth_date
		self.initial['user_photo'] = profile_instance.user_photo
		self.initial['email'] = profile_instance.email
		self.initial['phone_number'] = profile_instance.phone_number
		self.initial['street'] = profile_instance.street
		self.initial['city'] = profile_instance.city
		self.initial['state'] = profile_instance.state
		self.initial['zip_code'] = profile_instance.zip_code

	class Meta:
		model = UserProfile
		fields = ['first_name', 'last_name','birth_date','user_photo',
				  'email', 'phone_number', 'street', 'city', 'state',
				  'zip_code']