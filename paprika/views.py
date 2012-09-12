from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

def home(request):
  return render(request, 'home.html')
