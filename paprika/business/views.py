# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect

@login_required(login_url='/')
def orders(request, order_state):
  if request.method == 'GET':
    from paprika.models import Order, BusinessProfile

    # filtering through different order states
    orders = Order.objects.filter(merchant=request.user, state=order_state)

    return render_to_response('orders.html', {'user' : request.user, 'orders' : orders}, context_instance=RequestContext(request))
  elif request.method == 'POST':
    from paprika.business.forms import OrderForm
    order = OrderForm(request.POST)
    if not order.is_valid():
      return HttpResponse("not valid!" + request.POST.get('cust_name'))
    else:
      return HttpResponse('added order!')
  else:
    return HttpResponseBadRequest()

@login_required(login_url='/')
def flows(request):
  return render(request, 'flows.html')

@login_required(login_url='/')
def account(request):
  return render(request, 'account.html')
