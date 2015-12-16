#coding:utf-8
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render,render_to_response
from django.contrib import auth
from django.contrib.auth.models import User
from .models import artical
from .models import message
from .forms import messageForm,loginForm,userForm



# Create your views here.
def index(request):
	a1 = artical.objects.filter(slug="1")
	a2 = artical.objects.filter(slug="2")
	a3 = artical.objects.filter(slug="3")
	f1 = loginForm()
	f2 = userForm()
	return render(request, 'index.html',{
		'request': request,
		'artical1': a1,
		'artical2': a2,
		'artical3': a3,
		'form1': f1,
		'form2': f2,
		})

def contact(request):
	if request.method == 'POST':
		form = messageForm(request.POST)
		if form.is_valid():
			n = form.cleaned_data['name']
			m = form.cleaned_data['mail']
			p = form.cleaned_data['phone']
			me = form.cleaned_data['content']
			ss = message(name=n)
			ss.mail = m
			ss.phone = p
			ss.content = me
			ss.save()
			return HttpResponse('excellent')
		else:
			return HttpResponse('hehe')
	else:
		f = messageForm()
		f1 = loginForm()
		f2 = userForm()
		return render(request, 'contact.html', {
			'request': request,
			'form': f,
			'form1': f1,
			'form2': f2,
			})

def term(request):
	f1 = loginForm()
	f2 = userForm()
	return render(request, 'terms.html',{
		'request': request,
		'form1': f1,
		'form2': f2,
		})

def login(request):
	if request.method == 'POST':
		if not request.POST.get('username'):  
			errors.append('Please Enter username')
		else:
			usernm = request.POST.get('username')
		if not request.POST.get('password'):  
			errors.append('Please Enter password')
		else:
			passwd = request.POST.get('password')
		match = auth.authenticate(username=usernm, password=passwd)
		if match:
			auth.login(request, match)
			return HttpResponseRedirect('/index')
		else:
			return HttpResponse('Something wrong!')

def logout(request):
	auth.logout(request)
	return HttpResponseRedirect('/index')

def regist(request):
	if request.method == 'POST':
		usernm = request.POST.get('username')
		mail = request.POST.get('email')
		passwd = request.POST.get('password')
		passwd2 = request.POST.get('password2')
		if passwd == passwd2:
			newuser = User.objects.create_user(usernm,mail,passwd)
			newuser.is_active = True  
			newuser.save()
			return HttpResponse('You have signed in!')
		else:
			return HttpResponse('you failed')