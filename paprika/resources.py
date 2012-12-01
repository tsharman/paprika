from tastypie.resources import ModelResource, ALL
from tastypie import fields
from paprika.models import *
from tastypie.authorization import Authorization
from tastypie.authentication import BasicAuthentication
from django.forms import ModelForm
#from paprika.api.validation import ModelFormValidation

class StageResource(ModelResource):
    class Meta:
        resource_name = 'stage'
        queryset = Stage.objects.all()
        detail_allowed_methods = []
        list_allowed_methods = ['get']
        authorization = Authorization()
        authentication = BasicAuthentication()
        include_resource_uri = True

class FlowResource(ModelResource):
    class Meta:
        resource_name = 'flow'
        queryset = Flow.objects.all()
        detail_allowed_methods = []
        list_allowed_methods = ['get']
        authorization = Authorization()
        authentication = BasicAuthentication()
        include_resource_uri = True
    stages = fields.ToManyField(StageResource, 'stages', full=True)

class FeedEntryResource(ModelResource):
    class Meta:
        queryset = FeedEntry.objects.all()
        detail_allowed_methods = []
        list_allowed_methods = ['post']
        include_resource_uri = False
        resource_name = 'feed'
        authorization = Authorization()
        authentication = BasicAuthentication()

    #must make sure only can make a feed if authorized for that order's user
    #def obj_create(self, bundle, request=None, **kwargs):
    #    return super(OrderResource, self).obj_create(bundle, request, merchant=request.user.business)

class OrderResourceForm(ModelForm):
    class Meta:
        model = Order

class OrderResource(ModelResource):
    class Meta:
        queryset = Order.objects.all()
        detail_allowed_methods = ['get']
        list_allowed_methods = ['get','post']
        include_resource_uri = False
        #validation = ModelFormValidation(form_class=OrderResourceForm)
        resource_name = 'order'     
        authorization = Authorization() # no op authorization
        authentication = BasicAuthentication()
    flow = fields.ToOneField(FlowResource, 'flow', full=False)
    current_stage = fields.ToOneField(StageResource, 'current_stage', full=False)   
    feeds = fields.ToManyField(FeedEntryResource, 'feeds', full=True) 

    def determine_format(self, request):
        return "application/json"

    def obj_create(self, bundle, request=None, **kwargs):
        return super(OrderResource, self).obj_create(bundle, request, merchant=request.user.business)

    def apply_authorization_limits(self, request, object_list):
        return object_list.filter(merchant=request.user.business)

class BusinessProfileResource(ModelResource):
  class Meta:
    detail_allowed_methods = []
    list_allowed_methods = ['get']
    include_resource_uri = False
    queryset = BusinessProfile.objects.all()
    resource_name = 'profile'
    authentication = BasicAuthentication()
    authorization = Authorization()
  orders = fields.ToManyField(OrderResource, 'orders', full=True)
  flows = fields.ToManyField(FlowResource, 'flows', full=True)

  def determine_format(self, request):
    return "application/json"

  def apply_authorization_limits(self, request, object_list):
    return object_list.filter(user=request.user)



