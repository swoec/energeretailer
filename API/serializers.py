from rest_framework import serializers
from .models import Bill
from .models import Output


class BillSerializers(serializers.ModelSerializer):
    class Meta:
        model = Bill
        fields = ('icp_id', 'direction', 'interval_read', 'read_timestamp')


class OutputSerializers(serializers.ModelSerializer):
    class Meta:
        model = Output
        fields = ('icp_id', 'matched_amount', 'read_date', 'read_time', 'publish_datetime', 'buyer_seller')
