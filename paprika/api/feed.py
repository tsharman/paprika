from tastypie.resources import ModelResource, ALL
from tastypie import fields
from paprika.models import FeedEntry, Order
from paprika.api.businessprofile import OrderProxy 
from tastypie.authorization import Authorization
from tastypie.authentication import BasicAuthentication

class SimpleOrderProxy(ModelResource):
  class Meta:
    queryset = Order.objects.all()
    fields = ['cust_name', 'cust_phone', 'cust_email', 'time_entered', 'state', 'id']
    include_resource_uri = False

class FeedResource(ModelResource):
    class Meta:
        queryset = FeedEntry.objects.all()
        detail_allowed_methods = ['get']
        list_allowed_methods = ['post']
        include_resource_uri = False
        resource_name = 'feed'
        authorization = Authorization()
        authentication = BasicAuthentication()
    order = fields.ToOneField(SimpleOrderProxy, 'order', full=True)