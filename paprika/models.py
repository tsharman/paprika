from django.db import models
from django.contrib.auth.models import User
from django.contrib.localflavor.us.models import PhoneNumberField
from django.contrib import admin

class BusinessProfile(models.Model):
  user = models.OneToOneField(User, primary_key=True, related_name='business')
  business_name = models.CharField(max_length=100, blank=False)
  deleted = models.BooleanField(default=False)
  def __unicode__(self):
    return self.business_name

class Flow(models.Model):
  flow_name = models.CharField(max_length=100)
  owner = models.ForeignKey(BusinessProfile, related_name="flows")
  deleted = models.BooleanField(default=False)
  def sorted_stages(self):
    return self.stages.order_by('stage_num')

  def __unicode__(self):
    return "Flow " + self.flow_name

class Stage(models.Model):
  title = models.CharField(max_length=100)
  description = models.CharField(max_length=200)
  stage_num = models.IntegerField(default=1)
  flow = models.ForeignKey(Flow, related_name="stages")
  notes = models.CharField(max_length=300, blank=True)
  deleted = models.BooleanField(default=False)
  def __unicode__(self):
    return self.title

class Order(models.Model):
  flow = models.ForeignKey(Flow, related_name="orders")
  merchant = models.ForeignKey(BusinessProfile, related_name="orders")
  order_code = models.CharField(max_length=40, default='')
  current_stage = models.ForeignKey(Stage)
  cust_name = models.CharField(max_length=50)
  cust_phone = PhoneNumberField(default='0000000000')
  cust_email = models.EmailField(max_length=254, default='')
  notes = models.CharField(max_length=300, default='', blank=True)
  time_entered = models.DateTimeField(auto_now_add=True)
  STATE_CHOICES = (
    ('current', 'current'),
    ('done', 'done'),
    ('canceled', 'canceled'),
  )
  state = models.CharField(max_length = 10, choices = STATE_CHOICES, default='current')
  def __unicode__(self):
    return "Order " + self.order_code


admin.site.register(Order)
admin.site.register(Flow)
admin.site.register(Stage)
admin.site.register(BusinessProfile)
