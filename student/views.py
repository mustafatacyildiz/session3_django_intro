from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse('Hello world....')

def mustafa(request):
    return HttpResponse('My name is mustafa....')
