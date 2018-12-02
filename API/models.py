# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Create your models here.

from django.db import models


# Create your models here.
class Bill(models.Model):
    icp_id = models.IntegerField()
    direction = models.CharField(max_length=5)
    interval_read = models.DecimalField(max_digits=12, decimal_places=4)
    read_timestamp = models.DateTimeField(max_length=40)

    def __unicode__(self):
        return self.icp_id


class Output(models.Model):
    icp_id = models.IntegerField()
    matched_amount = models.DecimalField(max_digits=12, decimal_places=4)
    read_date = models.DateField(max_length=20)
    read_time = models.CharField(max_length=10)
    publish_datetime = models.DateTimeField(max_length=40)
    buyer_seller = models.CharField(max_length=12)

    def __unicode__(self):
        return self.icp_id
