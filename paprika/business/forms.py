from django.forms import ModelForm
from paprika.models import Order

class OrderForm(ModelForm):
	def __init__(self, *args, **kwargs):
		super(OrderForm, self).__init__(*args, **kwargs)
		self.fields['cust_phone'].required = False
		self.fields['cust_email'].required = False

	class Meta:
		model = Order
		exclude = ('merchant', 
			'current_stage',
			'notes',
			'state')
