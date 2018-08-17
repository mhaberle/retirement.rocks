from django.contrib import admin

from .models import UserProfile, UserExperience, UserRating

admin.site.register(UserProfile)
admin.site.register(UserExperience)
admin.site.register(UserRating)
