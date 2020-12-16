from django.shortcuts import render
from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import  AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.urls import reverse
# Create your views here.

def homepage(request):
	return render(request=request,
		          template_name="EventHub/home.html")