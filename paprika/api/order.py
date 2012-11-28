from tastypie.resources import ModelResource
from tastypie import fields
from paprika.models import Order, FeedEntry
from tastypie.authorization import Authorization
from tastypie.authentication import BasicAuthentication

class OrderAuthorization(Authorization):
    def is_authorized(self, request, **kwargs):
        if request.user == 2010:
            return True
        else:
            return False

class FeedProxy(ModelResource):
    class Meta:
        queryset = FeedEntry.objects.all()
        fields = ['body', 'time_entered']
        include_resource_uri = False
        

class OrderResource(ModelResource):
    class Meta:
        queryset = Order.objects.all()
        detail_allowed_methods = ['get']
        list_allowed_methods = ['post']
        include_resource_uri = False
        resource_name = 'order'
        authorization = Authorization()
        authentication = BasicAuthentication()
    feeds = fields.ToManyField(FeedProxy, 'feeds', full=True)
