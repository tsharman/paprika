from django.contrib.auth.decorators import login_required
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect
from paprika.models import Flow, Stage, Order, BusinessProfile
from paprika.business.forms import OrderForm
from django.contrib.auth.models import User

@login_required(login_url='/')
def orders(request, order_state):
  if request.method == 'GET': #render orders page
    their_orders = Order.objects.filter(merchant=request.user, state=order_state).order_by('-time_entered')
    return render_to_response('orders.html', {'user' : request.user, 'orders' : their_orders}, context_instance=RequestContext(request))
  
  elif request.method == 'POST': #add new order
    form = OrderForm(request.POST)
    if not form.is_valid():
			return HttpResponse("Form is not valid.")
    order = form.save(commit=False)
    
    order.merchant = BusinessProfile.objects.get(user=request.user)
    order.current_stage = order.flow.stages.get(stage_num=1)
		
		#verify method of contact
    if order.cust_phone == '' and order.cust_email == '':
			return HttpResponse("Must have a method of contact.")
		
    order.save()
    return HttpResponseRedirect('/bu/orders/')
  
  else:
    return HttpResponseBadRequest()

@login_required(login_url='/')
def flows(request):
  if request.method == 'GET':
    return render(request, 'flows.html')
  elif request.method == 'POST':
    flow_name = request.POST.get('flow_name')
    stage_titles = request.POST.getlist('stage_titles')
    stage_descriptions = request.POST.getlist('stage_descriptions')
    
    flow = Flow(flow_name = flow_name, owner = request.user.business)  
    flow.save()  

    for (counter, stage) in enumerate(stage_titles):
      new_stage = Stage(title = stage_titles[counter], description = stage_descriptions[counter], stage_num = (counter + 1), flow = flow)
      new_stage.save()
      
      
    return HttpResponseRedirect("/bu/flows/")

@login_required(login_url='/')
def account(request):
	if request.method == 'GET': #render account page
		return render_to_response('account.html', {'user' : request.user}, context_instance=RequestContext(request))

	elif request.method == 'POST': #update account
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
		
		#refresh page
		return render_to_response('account.html', {'user' : request.user}, context_instance=RequestContext(request))
  
