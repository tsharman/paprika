from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect
from django.forms import ValidationError
from paprika.models import Order, Flow, BusinessProfile, FeedEntry
from paprika.business.forms import OrderForm
from django.shortcuts import render_to_response

def move_stage(request):
  if request.method == 'POST':
    new_stage_index = request.POST.get('stage_index')
    order_id = request.POST.get('order_id')

    # retreiving the order
    order = Order.objects.get(id = order_id)

    # updating the current stage
    order.current_stage_id = new_stage_index

    # saving the order
    order.save()

    return HttpResponse(new_stage_index + " " + order.cust_name)
  else:
    return HttpResponseBadRequest()

def set_state(request):
  if request.method == 'POST':
    order_id = request.POST.get('order_id')
    new_state = request.POST.get('new_state')

    order = Order.objects.get(id = order_id)
    order.state = new_state.lower()
    order.save()

    return HttpResponse(order.cust_name)
  else:
    return HttpResponseBadRequest();

def delete_flow(request):
  if request.method == 'POST':
    flow_id = request.POST.get('flow_id')
    flow = Flow.objects.get(id = flow_id)
    flow.deleted = True
    flow.save()
    return HttpResponse()
  else:
    return HttpResponseBadRequest()

def delete_order(request):
  if request.method == 'POST':
    order_id = request.POST.get('order_id')
    order = Order.objects.get(id = order_id)
    order.state = 'canceled'
    order.save()
    return HttpResponse()
  else:
    return HttpResponseBadRequest()

def edit_order(request):
  if request.method == 'GET':
    order_id = request.GET.get('order_id')
    order = Order.objects.get(id = order_id)
    return HttpResponse(order.jsonify(), mimetype='application/json')
  elif request.method == 'POST':
    order = Order.objects.get(id=request.POST.get('order_id'))

    flow_id = order.flow.id

    form_args = { "flow" : flow_id }
    form_args.update(request.POST)

    #print "args %s" % form_args
    print "args %s" % request.POST

    form = OrderForm(request.POST, instance=order)
    print form
    if not form.is_valid():
      return HttpResponseBadRequest(form.errors)

		#verify method of contact
    if order.cust_phone == '' and order.cust_email == '':
			return HttpResponseBadRequest("Must have a method of contact.")

    order.save()
    return HttpResponse()
  else:
    return HttpResponseBadRequest()


def feed(request):
  if request.method == 'GET':
    order_id = request.GET.get('order_id')
    entries = Order.objects.get(id = order_id).feeds.order_by('-time_entered').all
    return render_to_response('fragments/feed.html', {'entries': entries})
  elif request.method == 'POST':
    order_id = request.POST.get('order_id')
    body = request.POST.get('body')
    feed_entry = FeedEntry(body = body, order_id = order_id)
    feed_entry.save()
    
    # constructing entries list with only one entry
    entries = [feed_entry,]
    
    #rendering with html, should only return a single feed_entry div
    return render_to_response('fragments/feed.html', {'entries': entries})
  else:
    return HttpResponseBadRequest() 
