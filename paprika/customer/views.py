# Create your views here.
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from paprika.models import Order

def search(request):
  if request.method == 'GET':
    return render_to_response('search.html', {}, context_instance=RequestContext(request)) 
  elif request.method == 'POST':
    search_query = request.POST.get('search_query')
    results = Order.objects.filter(cust_phone = search_query)
    return render_to_response('search.html', { 'search_results' : results}, context_instance=RequestContext(request))
  else:
    return HttpResponseBadRequest()

