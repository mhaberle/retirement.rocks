from django.db import models

from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save

from datetime import datetime

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

	EXPERIENCE_CHOICES = (
		('0-5','0-5'),('5-10','5-10'),('10-15','10-15'),('15-20','15-20'),('20-25','20-25'),('25-30','25-30'),('30 or more','30 or more'),
		)
	experience_length = models.CharField("years of work experience", max_length=10, choices=EXPERIENCE_CHOICES, default='0-5')
	experience_description = models.TextField("description of experience") #1-2 sentences of professional experience

	OPPORTUNITY_CHOICES = (
		('freelancing', 'freelancing'),('volunteering', 'volunteering'),('both', 'both'),
		)
	opportunity_type = models.CharField("opportunity type", max_length=50, choices=OPPORTUNITY_CHOICES, default='freelancing')

	def __str__(self):
		return self.user.email

class Experience(models.Model):
	#user tied to
	user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

	#experience details
	company = models.CharField("previous employer", max_length=100)	
	position = models.CharField("previous employer", max_length=100)
	start_date = models.DateField(verbose_name="start date", default=datetime.now)
	end_date = models.DateField(verbose_name="end date", default=datetime.now)
	experience_description = models.TextField("experience description")

class Rating(models.Model):
	#user being rated
	user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_being_rated')

	#user doing the rating
	employer = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='employer_rating_user')

	#rating details
	RATING_CHOICES = (
		('0','0'),('1','1'),('2','2'),('3','3'),('4','4'),('5','5'),
		)
	rating = models.CharField("rating", max_length=50, choices=RATING_CHOICES, default='5')
	rating_description = models.TextField("rating description")

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def save_user_profile(sender, instance, **kwargs):
	instance.profile.save()