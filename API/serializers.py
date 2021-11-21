from rest_framework import serializers
from .models import DataPacket
from .sensor_list import sensor_list


class DataPacketSerializer(serializers.ModelSerializer):
    """
    serializes the data into json format accepted by DataPacket table
    """
    class Meta:
        model = DataPacket
        fields = tuple(sensor_list)
