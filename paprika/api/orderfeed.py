from tastypie.resources import ModelResource
from tastypie import fields
from paprika.models import Order, FeedEntry
from tastypie.authorization import DjangoAuthorization
from tastypie.authentication import BasicAuthentication

class FeedProxy(ModelResource):
    class Meta:
        queryset = FeedEntry.objects.all()
        fields = ['body', 'time_entered']
        include_resource_uri = False
        

class OrderFeedResource(ModelResource):
    class Meta:
        queryset = Order.objects.all()
        detail_allowed_methods = ['get']
        list_allowed_methods = []
        include_resource_uri = False
        resource_name = 'feed'
        authorization = DjangoAuthorization()
        authentication = BasicAuthentication()
    feeds = fields.ToManyField(FeedProxy, 'feeds', full=True)
