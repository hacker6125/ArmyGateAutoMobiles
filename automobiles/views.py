from django import http
from django.urls import include
from django.shortcuts import render, redirect
from formdata.models import UserForm
from django.http import HttpResponse

def homeView(request):
	return render(request, 'index.html')

def FormSub(request):
	if request.method == 'POST':
		name = request.POST.get('name')
		email = request.POST.get('email')
		phno = request.POST.get('phno')
		msg = request.POST.get('msg')

		person = UserForm.objects.create(name=name, email=email, phno=phno, msg=msg)
		person.save()
		return redirect('/')


	else:
		return HttpResponse(request, 'method not allowed')