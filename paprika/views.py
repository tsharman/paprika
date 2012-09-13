from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
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
        return HttpResponseRedirect('/u/' + user.username)
      else:
        return HttpResponse('You have been banned!')
    else:
      return HttpResponse('Login Failed!')
  else:
    return HttpResponseRedirect('/')

def signout(request):
  logout(request)
  return HttpResponse('logged out!')

@login_required(login_url='/')
def user(request, username):
  return render(request, 'user.html', {
      'username' : username
    }) 
