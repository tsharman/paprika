from django.contrib.auth.decorators import login_required
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect
from django.contrib.auth.models import User
from paprika.models import Order, BusinessProfile

@login_required(login_url='/')
def orders(request, order_state):
  if request.method == 'GET':
    # filtering through different order states
    orders = Order.objects.filter(merchant=request.user.business, state=order_state)
    

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
	return render_to_response(request, 'account.html');

#	if request.method == 'GET':
#		#look up buisness name
#		business_profile = BusinessProfile.objects.get(user=request.user);
#		buisnes_name = business_profile.business_name	
#		return render_to_response(request, 'account.html', {'buisnes_name' : buisnes_name}) #  # context_instance?
#  elif request.method == 'POST':
#      return HttpResponse('account view recieved a POST request')
#	else:
#    return HttpResponseBadRequest()
