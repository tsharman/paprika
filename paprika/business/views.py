# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect
from paprika.models import Order, BusinessProfile
from paprika.business.forms import OrderForm

@login_required(login_url='/')
def orders(request, order_state):
  if request.method == 'GET':
    # filtering through different order states
    their_orders = Order.objects.filter(merchant=request.user, state=order_state)

    return render_to_response('orders.html', {'user' : request.user, 'orders' : their_orders}, context_instance=RequestContext(request))
  elif request.method == 'POST':
    form = OrderForm(request.POST)
    if not form.is_valid():
      print form.errors
      print "check it: %s" % form.is_bound
      return HttpResponse("not valid!" + request.POST.get('cust_name'))
    else:
      order = form.save(commit=False)
      order.merchant = BusinessProfile.objects.get(user=request.user)
      order.current_stage = order.flow.stages.get(stage_num=1)
      order.save()
      return HttpResponse('added order!')
  else:
    return HttpResponseBadRequest()

@login_required(login_url='/')
def flows(request):
  return render(request, 'flows.html')

@login_required(login_url='/')
def account(request):
  return render(request, 'account.html')
