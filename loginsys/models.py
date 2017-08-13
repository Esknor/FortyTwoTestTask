from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
	class Meta:
		db_table = "users_profiles"
	user_profile = models.OneToOneField(User)
	name = models.CharField(max_length=40, blank=True)
	last_name = models.CharField(max_length=40, blank=True)
	date_of_birth = models.DateTimeField(blank=True, null=True)
	email = models.CharField(max_length=40, blank=True)
	jabber = models.CharField(max_length=40, blank=True)
	skype = models.CharField(max_length=40, blank=True)
	other_contats = models.TextField()
	bio = models.TextField()
	

