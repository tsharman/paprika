from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect
from paprika.models import Order, Flow

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
    flow_id = request.POST.get('flow_id');
    flow = Flow.objects.get(id = flow_id)
    flow.deleted = True
    flow.save()
    return HttpResponse();
  else:
    return HttpResponseBadRequest();

def delete_order(request):
  if request.method == 'POST':
    order_id = request.POST.get('order_id');
    order = Order.objects.get(id = order_id)
    order.state = 'canceled'
    order.save()
    return HttpResponse();
  else:
    return HttpResponseBadRequest();
