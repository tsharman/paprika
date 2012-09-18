# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required(login_url='/')
def orders(request):
  return render(request, 'orders.html')

@login_required(login_url='/')
def flows(request):
  return render(request, 'flows.html')

@login_required(login_url='/')
def account(request):
  return render(request, 'account.html') 
