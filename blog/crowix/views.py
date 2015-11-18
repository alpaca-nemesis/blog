#coding:utf-8
from django.http import HttpResponse
from django.shortcuts import render
from .models import artical
from .models import message
from .forms import messageForm

# Create your views here.
def index(request):
	a1 = artical.objects.filter(slug="1")
	a2 = artical.objects.filter(slug="2")
	a3 = artical.objects.filter(slug="3")
	return render(request, 'index.html',{
		'artical1': a1,
		'artical2': a2,
		'artical3': a3,
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
		return render(request, 'contact.html', {'form': f})

def term(request):
	return render(request, 'terms.html')