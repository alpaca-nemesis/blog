#coding:utf-8
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')


def contact(request):
    return render(request, 'contact.html')


def term(request):
    return render(request, 'terms.html')