from tastypie.resources import ModelResource
from tastypie import fields
from paprika.models import *
from tastypie.authorization import Authorization
from tastypie.authentication import BasicAuthentication
from django.forms import ModelForm
from paprika.validation import ModelFormValidation

class BusinessProfileResource(ModelResource):
  class Meta:
    resource_name = 'profile'
    queryset = BusinessProfile.objects.all()
    detail_allowed_methods = []
    list_allowed_methods = ['get']
    authentication = BasicAuthentication()
    authorization = Authorization()
  orders = fields.ToManyField("paprika.resources.OrderProxyResource", 'orders', full=True)

  def determine_format(self, request):
    return "application/json"

  def apply_authorization_limits(self, request, object_list):
    return object_list.filter(user=request.user)


class OrderProxyResource(ModelResource):
    class Meta:
        queryset = Order.objects.all()

class OrderResourceForm(ModelForm):
    class Meta:
        model = Order

#Order Resource is the endpoint for creating an Order, 
#which belongs to a particular flow and business
class OrderResource(ModelResource):
    class Meta:
        resource_name = 'order'   
        queryset = Order.objects.all()
        detail_allowed_methods = ['get']
        list_allowed_methods = ['post']
        validation = ModelFormValidation(form_class=OrderResourceForm)
        authorization = Authorization() # no op authorization
        authentication = BasicAuthentication()
    flow = fields.ToOneField("paprika.resources.FlowResource", 'flow', full=True)   
    merchant = fields.ToOneField("paprika.resources.BusinessProfileResource", 'merchant', full=False) 
    feeds = fields.ToManyField("paprika.resources.FeedEntryResource", 'feeds', full=True, blank=True) 
    current_stage = fields.ToOneField("paprika.resources.StageResource", 'current_stage', full=True)  

    def determine_format(self, request):
        return "application/json"

    def obj_create(self, bundle, request=None, **kwargs):
        return super(OrderResource, self).obj_create(bundle, request, merchant=request.user.business)


class StageResource(ModelResource):
    class Meta:
        resource_name = 'stage'
        queryset = Stage.objects.all()
        detail_allowed_methods = []
        list_allowed_methods = []
        authorization = Authorization()
        authentication = BasicAuthentication()
        include_resource_uri = True

class FlowResource(ModelResource):
    class Meta:
        resource_name = 'flow'
        queryset = Flow.objects.all()
        detail_allowed_methods = []
        list_allowed_methods = []
        authorization = Authorization()
        authentication = BasicAuthentication()
        include_resource_uri = True
    stages = fields.ToManyField("paprika.resources.StageResource", 'stages', full=True)

class FeedEntryResource(ModelResource):
    class Meta:
        resource_name = 'feed'
        queryset = FeedEntry.objects.all()
        detail_allowed_methods = []
        list_allowed_methods = ['post']
        include_resource_uri = False
        authorization = Authorization()
        authentication = BasicAuthentication()
    order = fields.ToOneField("paprika.resources.OrderResource", 'order', full=False)




