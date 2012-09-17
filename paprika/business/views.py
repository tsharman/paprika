# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required(login_url='/')
def orders(request):
  return render(request, 'orders.html') 
