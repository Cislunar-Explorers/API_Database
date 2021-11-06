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

import uuid


@api_view(['POST'])
def add_data(request):
  """
  for inserting new data
  """
  serial_data = DataPacketSerializer(data = request.data)
  if serial_data.is_valid():
    serial_data.save()
    return Response (serial_data.data, status=status.HTTP_201_CREATED)
  
  fail = {
    "data":"failure: fields not valid"
  }
  return JsonResponse(fail)


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
    "data":"all deleted. not recoverable :)"
  }
  return Response (status=status.HTTP_200_OK)

