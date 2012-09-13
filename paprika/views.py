from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

def home(request):
  return render(request, 'home.html')

def signin(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
      if user.is_active:
        login(request, user)
        return HttpResponse('logged in!')
      else:
        return HttpResponse('You have been banned!')
    else:
      return HttpResponse('Login Failed!')
  else:
    return HttpResponseRedirect('/') 
