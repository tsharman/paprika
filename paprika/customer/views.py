# Create your views here.
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.template import RequestContext

def search(request):
  if request.method == 'GET':
    return render_to_response('search.html', {}, context_instance=RequestContext(request)) 
  elif request.method == 'POST':
    return render_to_response('search.html', {}, context_instance=RequestContext(request))
  else:
    return HttpResponseBadRequest()

