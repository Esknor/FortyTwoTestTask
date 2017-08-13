from django.contrib import admin
from loginsys.models import UserProfile
from django.contrib.auth.models import User


admin.site.register(UserProfile)
