from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import  AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.urls import reverse
from .forms import NewUserForm
from django.utils import timezone
from datetime import date, timedelta
from django.db.models import Q

# Create your views here.
def home(request):
	return render(request=request,
		          template_name="EventHub/home.html")
def register(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f"New account created: {username}")
			return redirect("EventHub:login")
		else:
			for msg in form.error_messages:
				messages.error(request,f"{msg}:{form.error_messages[msg]}")
	form = NewUserForm
	return render(request,"EventHub/register.html", context={"form":form})
def logout_request(request):
	logout(request)
	messages.info(request, "Logged out succesfully!")
	return redirect("EventHub:login")
def login_request(request):
	if request.method == 'POST':
		form = AuthenticationForm(request=request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}")
				return HttpResponseRedirect(reverse("EventHub:eventpage"))
				
				
			else:
				messages.error(request, "Invalid username or password.")
		else:
			messages.error(request, "Invalid username or password.")

	form = AuthenticationForm()
	return render(request,
		          "EventHub/login.html",
				  context={"form":form})
def eventpage(request):
    return render(request=request,
		          template_name="EventHub/eventpage.html")
