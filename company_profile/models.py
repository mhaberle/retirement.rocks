from django.db import models

from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save

from datetime import datetime

class CompanyProfile(models.Model):
	#company identification data
	user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	company_name = models.CharField("company name", max_length=50)
	first_name = models.CharField("first name", max_length=50)
	last_name = models.CharField("last_name", max_length=50)
	company_photo = models.ImageField(upload_to='profile_image') #https://stackoverflow.com/questions/6396442/add-image-avatar-field-to-users-in-django

	#company contact information
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
	
	#professional information
	mission_statement = models.TextField("mission statement")
	business_description = models.TextField("description of business")

	ORGANIZATION_CHOICES = (
		('for profit', 'for profit'),('non-profit','non-profit'),
		)
	organization_type = models.CharField("organization type", max_length=50, choices=ORGANIZATION_CHOICES, default='for profit')

	EMPLOYEE_SIZE_CHOICES = (
		('0-25','0-25'),('26-50','26-50'),('51-100','51-100'),('101-200','101-200'),('200+','200+'),
		)
	employee_number = models.CharField("number of employees", max_length=10, choices=EMPLOYEE_SIZE_CHOICES, default='0-25')

	YEARS_IN_BUSINESS_CHOICES = (
		('0-5','0-5'),('6-10','6-10'),('11-15','11-15'),('16-20','16-20'),('21-25','21-25'),('26-30','26-30'),('31 or more','31 or more'),
		)
	years_in_business = models.CharField("years in business", max_length=10, choices=YEARS_IN_BUSINESS_CHOICES, default='0-5')
 
	def __str__(self):
		return self.user.email

class CompanyRating(models.Model):
	#user being rated
	user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='employer_being_rated')

	#user doing the rating
	employer = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_rating_employer')

	#rating details
	RATING_CHOICES = (
		('0','0'),('1','1'),('2','2'),('3','3'),('4','4'),('5','5'),
		)
	rating = models.CharField("rating", max_length=50, choices=RATING_CHOICES, default='5')
	rating_description = models.TextField("rating description")

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_profile(sender, instance, created, **kwargs):
	if created:
		CompanyProfile.objects.create(user=instance)

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def save_user_profile(sender, instance, **kwargs):
	instance.companyprofile.save()