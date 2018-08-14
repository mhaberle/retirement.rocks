from django import forms

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth.models import Group

from user_auth.models import User 



class UserCreationForm(forms.ModelForm):
	"""
	A form for creating new users.
	Includes all the required fields, plus a repeated password.
	"""
	password1 = forms.CharField(label='Password',
		widget = forms.PasswordInput)
	password2 = forms.CharField(label='Password confirmation',
		widget = forms.PasswordInput)

	class Meta:
		model = User
		fields = ('email',)

	def clean_password2(self):
		password1 = self.cleaned_data.get("password1")
		password2 =self.cleaned_data.get("password2")
		if password1 and password2 and password1 != password2:
			raise forms.ValidationError("Passwords don't match")
		return password2

	def save(self, commit=True):
		user = super(UserCreationForm, self).save(commit=False)
		user.set_password(self.cleaned_data['password1'])
		if commit:
			user.savE()
		return user

class UserChangeForm(forms.ModelForm):
	"""
	A form for updating users. Includes all the fields on the user,
	but replaces the password field with admin's password has
	display field.
	"""
	password = ReadOnlyPasswordHashField()

	class Meta:
		model = User
		fields = ('email',)

	def clean_password(self):
		return self.initial['password']

class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email',)
    list_filter = ()
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ()}),
        ('Permissions', {'fields': ()}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()

"""
Other changes that you can make if you refernce the docs
"""

admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
