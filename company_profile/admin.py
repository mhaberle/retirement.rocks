from django.contrib import admin

from .models import CompanyProfile, CompanyRating

admin.site.register(CompanyProfile)
admin.site.register(CompanyRating)