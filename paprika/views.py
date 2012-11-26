from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from paprika.models import BusinessProfile
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from paprika.forms import NewUserForm
from django.contrib.admin.views.decorators import staff_member_required
from datetime import date


def index(request):
  return render(request, 'index.html')

def investors(request):
  return render(request, 'investors.html')

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
      return HttpResponseRedirect('/login/')
  elif request.method == 'GET':
    return render(request, 'signin.html')
  else:
    return HttpResponseRedirect('/bu/')

def signout(request):
  logout(request)
  return HttpResponseRedirect('/')

@staff_member_required
def dash(request):
  users = User.objects.all()
  users_today = User.objects.filter(date_joined__gte = date.today())
  return render_to_response('dash.html', { "users" : users, "users_today" : users_today }, context_instance=RequestContext(request))

@login_required(login_url='/')
def orders(request):
  return render(request, 'orders.html')

