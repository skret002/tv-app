from django.shortcuts import render
from .models import Staff
from .serializers import StaffSerializer
from rest_framework import generics, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
# Create your views here.


class StaffViewSet(APIView):

    def get(self, request):
        queryset = Staff.objects.all()
        serializer_class = StaffSerializer(queryset, many=True)
        return Response(serializer_class.data)
