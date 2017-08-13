from django.shortcuts import render, render_to_response, redirect
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
#from django.views.decorators import csrf
from django.template.context_processors import csrf
from django.contrib.auth.models import User
from .models import UserProfile


def users(request):
	users = User.objects.all()
	username = auth.get_user(request).username
	return render_to_response('users.html', {'users': users, 'username': username})

def user_profile(request, user_id):
	username = auth.get_user(request).username
	user_profile = UserProfile.objects.get(user_profile_id=user_id)
	return render_to_response('user_profile_detail.html', {'user_profile':user_profile, 'username': username})


def login(request):
	args = {}
	args.update(csrf(request))
	if request.POST:
		username = request.POST.get('username', '')
		password = request.POST.get('password', '')
		user = auth.authenticate(username=username, password=password)
		if user is not None:
			auth.login(request, user)
			return redirect('/')
		else:
			args['login_error'] = "User not found"
			return render_to_response('login.html', args)
	else:
		return render_to_response('login.html', args)

def logout(request):
	auth.logout(request)
	return redirect('/')

def register(request):
	args = {}
	args.update(csrf(request))
	args['form'] = UserCreationForm()
	if request.POST:
		new_user_form = UserCreationForm(request.POST)
		if new_user_form.is_valid():
			new_user_form.save()
			new_user = auth.authenticate(username=new_user_form.cleaned_data['username'], password=new_user_form.cleaned_data['password2'])
			auth.login(request, new_user)
			return redirect('/')
		else:
			args['form'] = new_user_form
	return render_to_response('register.html', args)
