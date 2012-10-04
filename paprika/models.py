from django.db import models
from django.contrib.auth.models import User
from django.contrib.localflavor.us.forms import USPhoneNumberField
from django.contrib import admin

class BusinessProfile(models.Model):
  user = models.OneToOneField(User, primary_key=True, related_name="business")
  business_name = models.CharField(max_length=100, blank=False)

class Flow(models.Model):
  flow_name = models.CharField(max_length=100)
  owner = models.ForeignKey(BusinessProfile, related_name="flows")
  def sorted_stages(self):
    return self.stages.order_by('stage_num')

class Stage(models.Model):
  title = models.CharField(max_length=100)
  description = models.CharField(max_length=200)
  stage_num = models.IntegerField(default=1)
  notes = models.CharField(max_length=300, default='')
  flow = models.ForeignKey(Flow, related_name="stages")

class Order(models.Model):
  flow = models.ForeignKey(Flow, related_name="orders")
  merchant = models.ForeignKey(BusinessProfile, related_name="orders")
  order_code = models.CharField(max_length=40, default='')
  current_stage = models.ForeignKey(Stage)
  cust_name = models.CharField(max_length=50)
  cust_phone = USPhoneNumberField()
  cust_email = models.EmailField(max_length=254, default='')
  notes = models.CharField(max_length=300, default='')
  time_entered = models.DateTimeField(auto_now=True)
  STATE_CHOICES = (
    ('current', 'current'),
    ('done', 'done'),
    ('canceled', 'canceled'),
  )
  state = models.CharField(max_length = 10, choices = STATE_CHOICES, default='current')

admin.site.register(Order)
admin.site.register(Flow)
admin.site.register(Stage)
admin.site.register(BusinessProfile)
