from django.db import models
from django.conf import settings

from datetime import datetime

class PostDetail(models.Model):

	poster = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	post_name = models.CharField("post name", max_length=50)

	#need to make the following an 'if statement' so that for profit companies can't post for volunteers
	POST_TYPE_CHOICES = (
		('for pay', 'for pay'),('volunteer','volunteer'),
		)
	post_type = models.CharField("post type", max_length=50, choices=POST_TYPE_CHOICES, default='for pay')
	post_start_date = models.DateField(verbose_name="start date", default=datetime.now)
	post_end_date = models.DateField(verbose_name="end date", default=datetime.now)	
	post_details = models.TextField("post details")
	experience_description = models.TextField("experience description")

	WORK_LOCATION_CHOICES = (
		('from your home', 'from your home'),('at the office','at the office'),
		)
	work_location = models.CharField("work location", max_length=50, choices=WORK_LOCATION_CHOICES, default='for profit')
	date_posted = models.DateField(auto_now_add=False) # to remove from the list at certain date

	CANDIDATE_ACCEPTED_CHOICES = (
		('yes', 'yes'),('no','no'),
		)
	candidate_accepted = models.CharField("have you accpeted a candidate", max_length=50, choices=CANDIDATE_ACCEPTED_CHOICES, default='no') #will remove posting once a candidate has been accepted or no longer accepting candidates

	def __str__(self):
		return self.post_name

class ProjectRate(models.Model):

	post_name = models.OneToOneField(PostDetail, on_delete=models.CASCADE) 
	rate = models.IntegerField("pay rate per hour")
	hours = models.IntegerField("hours")

	def __str__(self):
		return self.post_name