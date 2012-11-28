from tastypie.resources import ModelResource, ALL
from tastypie import fields
from paprika.models import Flow, Stage
from paprika.api.businessprofile import OrderProxy 
from tastypie.authorization import Authorization
from tastypie.authentication import BasicAuthentication
 

class FlowResource(ModelResource):
    class Meta:
        queryset = Flow.objects.all()
        detail_allowed_methods = ['get']
        list_allowed_methods = ['get']
        include_resource_uri = False
        resource_name = 'flow'
        authorization = Authorization()
        authentication = BasicAuthentication()
