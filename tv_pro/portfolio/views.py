from django.shortcuts import render
from .models import Portfolio, PortfolioImg
from .serializers import PortfolioSerializer, PortfolioImgSerializer
from rest_framework import generics, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
# Create your views here.


class PortfolioImgViewSet(APIView):

    def post(self, request):
        queryset = PortfolioImg.objects.filter(portfolio__id=request.data['params']['data'][0]["id"])
        serializer_class = PortfolioImgSerializer(queryset, many=True)
        return Response(serializer_class.data)


class PortfolioViewSet(APIView):

    def post(self, request):
        s = request.data['params']['data'][0]['start']
        e=request.data['params']['data'][0]['end']
        queryset = Portfolio.objects.all()[s:e]
        serializer_class = PortfolioSerializer(queryset, many=True)
        return Response(serializer_class.data)
