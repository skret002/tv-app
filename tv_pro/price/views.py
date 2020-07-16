from django.shortcuts import render
from .models import Price, TypeLcd, TvBrend, Malfunks, TvSizePrice
from .serializers import PriceSerializer, TypeLcdSerializer, TvSizePriceSerializer
from rest_framework import generics, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
# Create your views here.

class PriceViewSet(APIView):

    def post(self, request):
        queryset = Price.objects.filter(brend_size__type_lcd__id=request.data['params']['id'])
        serializer_class = PriceSerializer(queryset, many=True)
        return Response(serializer_class.data)


class MulfunkViewSet(APIView):
    def post(self, request):
        queryset = TvSizePrice.objects.filter(malfunk__price__brend_size__brend_name_id=request.data['params']['data']['data'][0],
                                              malfunk__malfunk=request.data['params']['data']['data'][1])
        serializer_class = TvSizePriceSerializer(queryset, many=True)
        return Response(serializer_class.data)

class TypeLcdViewSet(viewsets.ModelViewSet):
     queryset = TypeLcd.objects.all()
     serializer_class = TypeLcdSerializer
