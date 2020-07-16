from django.shortcuts import render
from .models import Home, SlideInHome, TypesOfMalfunctions, AboutInHome, InfoAboutOrder, Reviews
from .serializers import HomeSerializer, TypesOfMalfunctionsSerializer, AboutInHomeSerializer, InfoAboutOrderSerializer, ReviewsSerializer
from rest_framework import generics, viewsets
from django.http import HttpResponseRedirect
# Create your views here.


class ReviewsViewSet(viewsets.ModelViewSet):
     queryset = Reviews.objects.all()
     serializer_class = ReviewsSerializer


class HomeViewSet(viewsets.ModelViewSet ):
     queryset = Home.objects.all()
     serializer_class = HomeSerializer


class MalfunctionsViewSet(viewsets.ModelViewSet):
     queryset = TypesOfMalfunctions.objects.all()
     serializer_class = TypesOfMalfunctionsSerializer


class AboutInHomeViewSet(viewsets.ModelViewSet):
     queryset = AboutInHome.objects.all()
     serializer_class = AboutInHomeSerializer


class InfoAboutOrderSerializerViewSet(viewsets.ModelViewSet):
     queryset = InfoAboutOrder.objects.all()
     serializer_class = InfoAboutOrderSerializer
