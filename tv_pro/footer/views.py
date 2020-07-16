from django.shortcuts import render
from .models import *
from .serializers import AdditionalStaffSerializer, SaleInFooterSerializer, CenterInFooterSerializer
from rest_framework import generics, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
# Create your views here.


class StaffViewSet(APIView):

    def post(self, request):
        queryset = AdditionalStaff.objects.all()
        serializer_class = AdditionalStaffSerializer(queryset, many=True)
        return Response(serializer_class.data)


class SaleInFooterViewSet(APIView):

    def get(self, request):
        queryset = SaleInFooter.objects.all()
        serializer_class = SaleInFooterSerializer(queryset, many=True)
        return Response(serializer_class.data)


class CenterInFooterViewSet(APIView):

    def get(self, request):
        queryset = CenterInFooter.objects.all()
        serializer_class = CenterInFooterSerializer(queryset, many=True)
        return Response(serializer_class.data)
