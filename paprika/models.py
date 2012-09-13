from django.db import models


class Flow(models.Model):
  flow_name = models.CharField(max_length=100)

class Stage(models.Model):
  title = models.CharField(max_length=100)
  description = models.CharField(max_length=200)
  stage_num = models.IntegerField()
  flow = models.ForeignKey(Flow)



