# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, render_to_response
from django.template import RequestContext

@login_required(login_url='/')
def orders(request):
  return render_to_response('orders.html', {}, context_instance=RequestContext(request))

@login_required(login_url='/')
def flows(request):
  return render(request, 'flows.html')

@login_required(login_url='/')
def account(request):
  return render(request, 'account.html') 
