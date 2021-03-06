# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import viewsets
from .serializers import BillSerializers
from .serializers import OutputSerializers
from django.db.models import Avg, Sum
from datetime import datetime
import timestring
from rest_framework import views, viewsets, authentication, permissions, pagination
from rest_framework.pagination import PageNumberPagination
import redis
from .models import Bill
from .models import Output
import datetime

redis_host = "localhost"
redis_port = 6379
redis_password = ""
try:
    r = redis.StrictRedis(host=redis_host, port=redis_port, password=redis_password, decode_responses=True)
except Exception as e:
    print(e)


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 10


class BillViewSet(viewsets.ModelViewSet):
    queryset = Bill.objects.get_queryset()
    serializer_class = BillSerializers

    def get_queryset(self):
        icp_id = self.request.query_params.get('icp_id')
        startdate = self.request.query_params.get('startdate')
        enddate = self.request.query_params.get('enddate')

        if icp_id is not None and startdate is not None and enddate is not None:
            queryset = Bill.objects.filter(icp_id=icp_id, read_timestamp__gte=startdate,
                                           read_timestamp__lte=enddate)

        return queryset


class OutputViewSet(viewsets.ModelViewSet):
    queryset = Output.objects.get_queryset()
    serializer_class = OutputSerializers

    def get_queryset(self):
        icp_id = self.request.query_params.get('icp_id')
        startdate = self.request.query_params.get('startdate')
        enddate = self.request.query_params.get('enddate')
        role = self.request.query_params.get('role')

        url = self.request.query_params

        if icp_id is not None and startdate is not None and enddate is not None and role is not None:

            output = Output
            output.icp_id = icp_id
            outputlist = []
            querysets = Bill.objects.filter(icp_id=icp_id, read_timestamp__gte=startdate, read_timestamp__lte=enddate,
                                            direction=role).aggregate(Sum('interval_read'))

            output = Output()
            output.icp_id = icp_id
            rdate = timestring.Date(startdate).date
            output.read_date = rdate.date()
            output.matched_amount = querysets['interval_read__sum']
            if role == 'x':
                output.buyer_seller = 'seller'
            else:
                output.buyer_seller = 'buyer'
            output.read_time = rdate.time()
            output.publish_datetime = datetime.datetime.now()
            output.save(self)

            outputlist.append(output)
            queryset = outputlist

        return queryset


class OutputPageViewSet(viewsets.ModelViewSet):
    queryset = Output.objects.get_queryset()
    serializer_class = OutputSerializers
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        icp_id = self.request.query_params.get('icp_id')
        outputlist = []
        querysets = Bill.objects.filter(icp_id=icp_id)

        for q in querysets:
            output = Output()
            output.icp_id = q.icp_id
            output.read_date = q.read_timestamp.date()
            output.matched_amount = q.interval_read
            role = q.direction
            if role == 'x':
                output.buyer_seller = 'seller'
            else:
                output.buyer_seller = 'buyer'
            output.read_time = q.read_timestamp.time()
            output.publish_datetime = datetime.datetime.now()
            output.save(self)
            outputlist.append(output)

        queryset = outputlist
        return queryset


class OutputKeyViewSet(viewsets.ModelViewSet):
    queryset = Output.objects.get_queryset()
    serializer_class = OutputSerializers
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        startdate = self.request.query_params.get('startdate')
        enddate = self.request.query_params.get('enddate')
        outputlist = []
        querysets = Bill.objects.filter(read_timestamp__gte=startdate, read_timestamp__lte=enddate).order_by('icp_id')
        for q in querysets:
            output = Output()
            output.icp_id = q.icp_id
            output.read_date = q.read_timestamp.date()
            output.matched_amount = q.interval_read
            role = q.direction
            if role == 'x':
                output.buyer_seller = 'seller'
            else:
                output.buyer_seller = 'buyer'
            output.read_time = q.read_timestamp.time()
            output.publish_datetime = datetime.datetime.now()
            output.save(self)
            outputlist.append(output)

        queryset = outputlist

        return queryset
