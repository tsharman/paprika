from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect
from paprika.models import Order

def move_stage(request):
  if request.method == 'POST':
    new_stage_index = request.POST.get('stage_index')  
    order_id = request.POST.get('order_id')

    order = Order.objects.get(id = order_id)
    order.current_stage_id = new_stage_index
    order.save()

    return HttpResponse(new_stage_index + " " + order.cust_name)
  else:
    return HttpResponseBadRequest()
