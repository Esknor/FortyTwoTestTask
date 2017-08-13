from django.conf.urls import url, include
from . import views

urlpatterns = [
	url(r'^$', views.users, name = 'users'),
	url(r'^login/', views.login, name = 'login'),
	url(r'^logout/', views.logout, name = 'logout'),
	url(r'^register/$', views.register, name='register'),
	url(r'^user_profile/(?P<user_id>\d+)/$', views.user_profile, name='user_profile'),
]
