from tastypie.resources import ModelResource, ALL
from tastypie import fields
from paprika.models import BusinessProfile, Order, Stage, Flow
from tastypie.authorization import Authorization


class StageProxy(ModelResource):
    class Meta:
        queryset = Stage.objects.all()
        fields = ['title', 'description', 'stage_num', 'notes', 'deleted']


class FlowProxy(ModelResource):
    class Meta:
        queryset = Flow.objects.all()
        fields = ['flow_name', 'owner', 'deleted']
    stages = fields.ToManyField(StageProxy, 'stages', full=True)


class OrderProxy(ModelResource):
    class Meta:
        queryset = Order.objects.all()
        fields = ['cust_name', 'cust_phone', 'cust_email', 'time_entered', 'state']
    flow = fields.ToOneField(FlowProxy, 'flow', full=True)


class BuisnessProfileResource(ModelResource):
    class Meta:
        detail_allowed_methods = ['get']
        list_allowed_methods = []
        authorization = Authorization()
        include_resource_uri = False
        queryset = BusinessProfile.objects.all()
        resource_name = 'business'
    orders = fields.ToManyField(OrderProxy, 'orders', full=True)

    def determine_format(self, request):
        return "application/json"
