from django.shortcuts import render
from django.http import HttpResponse
import random

def home(request):
	return render(request, 'generators/home.html')

def about(request):
	return render(request, 'generators/about.html')

def password(request):

	thepassword = ''
	lenght = int(request.GET.get('length', 12))

	characters = list('abcdefghijklmnopqrstuvwxyz')

	if request.GET.get('uppercase'):
		characters.extend(list('ABCDEFGHIGKLMNOPQRSTUVWXYZ'))
	if request.GET.get('numbers'):
		characters.extend(list('0123456789'))
	if request.GET.get('special'):
		characters.extend(list('!@#$%^&*()'))
	

	for x in range(lenght):
		thepassword += random.choice(characters)
	return render(request, 'generators/password.html', {'password' : thepassword})