from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect
from django.forms import ValidationError
from paprika.models import Order, Flow, BusinessProfile
from paprika.business.forms import OrderForm

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
    oldorder = Order.objects.get(id=request.POST.get('order_id'))
    cust_email = request.POST.get('cust_email')
    cust_phone = request.POST.get('cust_phone')
    cust_name = request.POST.get('cust_name')
    notes = request.POST.get('notes')

    newargs = {"flow": oldorder.flow.id, "order_code" : oldorder.order_code, "cust_name" : cust_name, "cust_phone" : cust_phone, "cust_email" : cust_email, "notes" : notes, "time_entered" : oldorder.time_entered}


    form = OrderForm(newargs)
    if not form.is_valid():
      return HttpResponseBadRequest(form.errors)
    neworder = form.save(commit=False)
    neworder.merchant = BusinessProfile.objects.get(user=request.user)
    neworder.current_stage = oldorder.flow.stages.get(stage_num=1)

		#verify method of contact
    if neworder.cust_phone == '' and neworder.cust_email == '':
			return HttpResponseBadRequest("Must have a method of contact.")

    neworder.save()
    oldorder.delete()
    return HttpResponse()
  else:
    return HttpResponseBadRequest()
