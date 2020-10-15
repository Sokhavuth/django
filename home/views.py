#home/views.py
from django.http import HttpResponse
from django.shortcuts import render

context = {'blogTitle':"Khmer Web", 'message':"Hello World!"}

def index(request):
  return render(request, 'index.html', context)
