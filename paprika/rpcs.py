from django.views.decorators.csrf import csrf_exempt
from paprika.utils.basicauth import authenticated
from paprika.models import Order, Stage, Flow
from django.http import HttpResponse, HttpResponseBadRequest
from django.utils import simplejson

@authenticated
def move_stage(request):
  if request.POST:
    try:
        json_data = simplejson.loads(request.raw_post_data)
        stage_num = json_data['stage_num']
        order_id = json_data['order_id']
        flow_id = json_data['flow_id']
    except:
        return HttpResponseBadRequest("missing fields")


    # retreiving the order
    order = Order.objects.get(id = order_id)

    # retreiving the flow
    flow = Flow.objects.get(id = flow_id)

    #retreiving stage
    stage = Stage.objects.get(flow = flow, stage_num = stage_num)

    # updating the current stage
    order.current_stage = stage

    # saving the order
    order.save()

    return HttpResponse()
  else:
    return HttpResponseBadRequest()


