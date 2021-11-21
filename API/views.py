from django.shortcuts import render

from django.shortcuts import render
from django.http.response import Http404
from django.shortcuts import render
from django.core import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.http import JsonResponse

from .models import DataPacket
from .serializers import DataPacketSerializer
from .sensor_list import sensor_list

import json

headers_app = {'Content-type': 'application/json'}

# -------------------------------------------------------------------
# endpoints for grafana connecton
# -------------------------------------------------------------------


@api_view(['GET'])
def test_connection(request):
    """
    required by grafana sources to test connection
    """
    return Response(status=status.HTTP_200_OK)


@api_view(['POST'])
def data_series(request):
    """
    return names of data series available
    """
    data_series_json = json.dumps(sensor_list)

    return Response(data=data_series_json, headers=headers_app)


@api_view(['POST'])
def handle_query(request):
    """
    checks which response grafana is requesting,
    then calls function to return appropriate response.
    """
    # table
    if request.json['targets'][0]['type'] == 'table':
        series = request.json['targets'][0]['target']
        data_json = json.dumps(table_format(series))
        return Response(data=data_json, headers=headers_app)

    # plot
    else:
        body = []
        start, end = request.json['range']['from'], request.json['range']['to']

        for target in request.json['targets']:
            series = target['target']
            datapoints = datapoints_format(series, start, end)
            body.append({
                'target': series,
                'datapoints': datapoints
            })
        data_json = json.dumps(body)

        return Response(data=json.dumps(), headers=headers_app)


# helper functions for table format

def table_format(series_name: str):
    """
    formats table body, using helper function rows_format
    """
    columns = [
        {"text": "Time", "type": "time"},
        {"text": series_name, "type": "number"}
    ]
    table = [{
        "columns": columns,
        "rows": rows_format(series_name),
        "type": "table"
    }]
    return table


def rows_format(field_name: str):
    """
    returns the column row format for the data field requested
    """
    data_query_set = DataPacket.objects.all().values_list(field_name)
    data_list = [datapoint for datapoint in list(data_query_set)]

    time_query_set = DataPacket.objects.all().values_list('time')
    time_list = [timepoint for timepoint in list(time_query_set)]

    table = []
    for i in range(len(data_list)):
        table_entry = [time_list[i], data_list[i]]
        table.append(table_entry)

    return table


# helper function for time series plot format

def datapoints_format(fieldname: str, start: int, end: int):
    backwards_list = rows_format(fieldname)

    datapoints = []
    for i in range(len(backwards_list)):
        time = backwards_list[i][0]*1000

        # TODO IMPORTANT: optimize by replacing this with a filter query!!!!!
        # read QuerySet API documentation : https://docs.djangoproject.com/en/3.2/ref/models/querysets/

        if (start < time < end):
            datap = [backwards_list[i][1], time]
            datapoints.append(datap)

    return datapoints


# -------------------------------------------------------------------
# endpoints for UDP connection
# -------------------------------------------------------------------

@api_view(['POST'])
def add_data(request):
    """
    for inserting new data
    """
    serial_data = DataPacketSerializer(data=request.data)
    if serial_data.is_valid():
        serial_data.save()
        return Response(serial_data.data, status=status.HTTP_201_CREATED)

    return JsonResponse(serial_data.error_messages)


@api_view(['GET'])
def get_data(request):
    """
    retrieve all data, in indexed nested json dictionary form

    note@myself: maybe fix this later so it only returns the data from the most recent 
    period of time.
    """
    all_data = DataPacket.objects.all()
    serial_all_data = DataPacketSerializer(all_data, many=True)
    return Response(serial_all_data.data)


@api_view(['DELETE'])
def delete_data(request):
    """
    deletes all data. Use only for testing. Data is not recoverable after deletion.
    """
    DataPacket.objects.all().delete()
    deleted = {
        "data": "all deleted. not recoverable :)"
    }
    return Response(data=json.dumps(deleted), status=status.HTTP_200_OK)
