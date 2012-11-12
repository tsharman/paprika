from tastypie.resources import ModelResource, ALL
from tastypie import fields
from paprika.models import BusinessProfile, Order, Stage, Flow
from tastypie.authorization import Authorization
from django.forms import ModelForm
#from novella.api.validation import ModelFormValidation 

class StageProxy(ModelResource):
	class Meta:
		queryset = Stage.objects.all()
		fields = ['title', 'description', 'stage_num', 'notes', 'deleted']

class FlowProxy(ModelResource):
	stages = fields.ToManyField(StageProxy, 'stages', full=True)
	class Meta:
		queryset = Flow.objects.all()
		fields = ['flow_name', 'owner', 'deleted']

class OrderProxy(ModelResource):
	flow = fields.ToOneField(FlowProxy, 'flow', full=True)
	class Meta: 
		queryset = Order.objects.all()
		fields = ['cust_name', 'cust_phone', 'cust_email', 'time_entered','state']

class BuisnessProfileResource(ModelResource):
	orders = fields.ToManyField(OrderProxy, 'orders', full=True)
	class Meta:
		detail_allowed_methods = ['get']
		list_allowed_methods = []
		authorization = Authorization()
		include_resource_uri = False
		queryset = BusinessProfile.objects.all()
		resource_name = 'business'
		filtering = {
			'merchant' : ALL
		}
	def determine_format(self, request):
		return "application/json"
