from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from paprika.models import BusinessProfile
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from paprika.forms import NewUserForm


def index(request):
  return render(request, 'index.html')

def signup(request):
  if request.method == 'POST':
    form = NewUserForm(request.POST)
    if form.is_valid():
      new_user = User.objects.create_user(form.cleaned_data['username'],form.cleaned_data['email'], form.cleaned_data['password'])
      business_prof = BusinessProfile(user=new_user, business_name=form.cleaned_data['business_name'])
      business_prof.save()
      return signin(request)
    else:
      return HttpResponseRedirect('/bu/')
  else:
    return HttpResponseBadRequest()
    return render(request, 'signup.html')

def signin(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
      if user.is_active:
        login(request, user)
        return HttpResponseRedirect('/bu/orders/')
      else:
        return HttpResponse('You have been banned!')
    else:
      return HttpResponse('Login Failed!')
  else:
    return HttpResponseRedirect('/bu/')

def signout(request):
  logout(request)
  return HttpResponseRedirect('/')

@login_required(login_url='/')
def orders(request):
  return render(request, 'orders.html')
