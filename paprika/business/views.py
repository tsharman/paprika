from django.contrib.auth.decorators import login_required
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect
from paprika.models import Order, BusinessProfile
from paprika.business.forms import OrderForm
from django.contrib.auth.models import User

@login_required(login_url='/')
def orders(request, order_state):
  if request.method == 'GET':
    # filtering through different order states
    their_orders = Order.objects.filter(merchant=request.user, state=order_state).order_by('-time_entered')

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
      return HttpResponseRedirect('/bu/orders/')
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

		#save business profile
		user.save()
		user.business.save()

		#refresh page
		return render_to_response('account.html', {'user' : request.user}, context_instance=RequestContext(request))

