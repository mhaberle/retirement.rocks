from django.db import models

from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save

from datetime import datetime
from phonenumber_field.modelfields import PhoneNumberField

class Profile(models.Model):
	#user identification data
	user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	first_name = models.CharField("first name", max_length=50)
	last_name = models.CharField("last_name", max_length=50)
	user_photo = models.ImageField(upload_to='profile_image') #https://stackoverflow.com/questions/6396442/add-image-avatar-field-to-users-in-django

	#user contact information
	
	email = models.EmailField("email", max_length=254)
	phone_number = models.CharField("phone number", max_length=11)
	
	#user address
	street = models.CharField("street address", max_length=100)
	city = models.CharField("city", max_length=100)

	STATE_CHOICES = (
		('AL','AL'),('AK','AK'),('AZ','AZ'),('AR','AR'),('CA','CA'),('CO','CO'),('CT','CT'),('DE','DE'),('FL','FL'),('GA','GA'),('HI','HI'),('ID','ID'),('IL','IL'),('IN','IN'),('IA','IA'),
		('KS','KS'),('KY','KY'),('LA','LA'),('ME','ME'),('MD','MD'),('MA','MA'),('MI','MI'),('MN','MN'),('MS','MS'),('MO','MO'),('MT','MT'),('NE','NE'),('NV','NV'),('NH','NH'),('NJ','NJ'),
		('NM','NM'),('NY','NY'),('NC','NC'),('ND','ND'),('OH','OH'),('OK','OK'),('OR','OR'),('PA','PA'),('RI','RI'),('SC','SC'),('SD','SD'),('TN','TN'),('TX','TX'),('UT','UT'),('VT','VT'),
		('VA','VA'),('WA','WA'),('WV','WV'),('WI','WI'),('WY','WY'),
		)
	state = models.CharField("state", max_length=50, choices=STATE_CHOICES, default='AL')
	zip_code = models.CharField("zip code", max_length=5)
	
	#other user attributes
	birth_date = models.DateField(verbose_name="birth date", default=datetime.now)
	
	#professional information
	mission_statement = models.TextField("mission statement") #1-2 sentences to sell yourself
	#(need to add choices) industry_of_experience = #drop down menu of general industries
	experience_description = models.TextField("description of experience") #1-2 sentences of professional experience
	#(need to add choices) experience_length = #menu of experience length (0-10, 10-20, 20-30, or more)
	#(need to add choices) opportunity_type = #freelancing, volunteering, or both


	#current_rating = will update based on a view that does the current math

	def __str__(self):
		return self.user.email

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def save_user_profile(sender, instance, **kwargs):
	instance.profile.save()