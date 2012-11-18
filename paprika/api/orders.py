from tastypie.resources import ModelResource, ALL
from tastypie import fields
from paprika.models import BusinessProfile, Order, Stage, Flow
from tastypie.authorization import Authorization
from tastypie.authorization import DjangoAuthorization
from paprika.authentication import TwoLeggedOAuthAuthentication

class StageProxy(ModelResource):
    class Meta:
        queryset = Stage.objects.all()
        include_resource_uri = False
        fields = ['title', 'description', 'stage_num', 'notes', 'deleted']


class FlowProxy(ModelResource):
    class Meta:
        queryset = Flow.objects.all()
        fields = ['flow_name', 'owner', 'deleted']
        include_resource_uri = False
    stages = fields.ToManyField(StageProxy, 'stages', full=True)


class OrderProxy(ModelResource):
    class Meta:
        queryset = Order.objects.all()
        fields = ['cust_name', 'cust_phone', 'cust_email', 'time_entered', 'state']
        include_resource_uri = False
    flow = fields.ToOneField(FlowProxy, 'flow', full=True)


class BusinessProfileResource(ModelResource):
    class Meta:
        detail_allowed_methods = ['get']
        list_allowed_methods = ['get']
        include_resource_uri = False
        queryset = BusinessProfile.objects.all()
        resource_name = 'business'
        authorization = DjangoAuthorization()
        authentication = TwoLeggedOAuthAuthentication()
    orders = fields.ToManyField(OrderProxy, 'orders', full=True)

    def determine_format(self, request):
        return "application/json"
