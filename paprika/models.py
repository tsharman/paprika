from django.db import models
from django.contrib.auth.models import User
from django.contrib.localflavor.us.forms import USPhoneNumberField

class Flow(models.Model):
  flow_name = models.CharField(max_length=100)
  owner = models.ForeignKey(User, related_name="flows")

class Stage(models.Model):
  title = models.CharField(max_length=100)
  description = models.CharField(max_length=200)
  stage_num = models.IntegerField()
  flow = models.ForeignKey(Flow, related_name="stages")

class Order(models.Model):
  flow = models.ForeignKey(Flow, related_name="orders")
  merchant = models.ForeignKey(User, related_name="orders")
  order_code = models.CharField(max_length=40)
  current_stage = models.ForeignKey(Stage)
  cust_name = models.CharField(max_length=50)
  cust_phone = USPhoneNumberField()
  cust_email = models.EmailField(max_length=254)

class BusinessProfile(models.Model):
  user = models.OneToOneField(User, primary_key=True)
  business_name = models.CharField(max_length=100, blank=False)



