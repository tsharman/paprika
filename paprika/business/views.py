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
	if request.method == 'GET':
		return render_to_response('account.html', {'user' : request.user}, context_instance=RequestContext(request))
	elif request.method == 'POST':
		user = request.user
		
		#get post data
		business_name = request.POST.get('business_name')
		user_name = request.POST.get('user_name')
		email = request.POST.get('email')
		new_password = request.POST.get('new_password')
		
		#update models
		user.business.business_name = business_name
		user.username = user_name
		user.email = email
		if new_password != "": #lame, will be better than this
			user.set_password(new_password); 
		
		#save models
		user.save()
		user.business.save()
		
		#refresh
		return render_to_response('account.html', {'user' : request.user}, context_instance=RequestContext(request))

