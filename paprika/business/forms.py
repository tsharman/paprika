from django.forms import ModelForm
from paprika.models import Order

class OrderForm(ModelForm):
  class Meta:
    model = Order
    exclude = ('merchant', 'notes', 'current_stage', 'state',)
