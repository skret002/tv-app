from django.shortcuts import render
from .models import Category, Parts, PartsImg, OrderShop, ProductInOrder
from .serializers import CategorySerializer, PartsSerializer, PartsImgSerializer
from rest_framework import generics, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.


class CategoryViewSet(APIView):

    def get(self, request):
        queryset = Category.objects.all()
        serializer_class = CategorySerializer(queryset, many=True)
        return Response(serializer_class.data)


class PartsViewSet(APIView):
    def post(self, request):
        print(request.data)
        if request.data['params']['search']:
            queryset = Parts.objects.filter(title__icontains=request.data['params']['search'])[:10]
        elif  request.data['params']['category']:
            queryset = Parts.objects.filter(category__title=request.data['params']['category'])
        else:
            queryset = Parts.objects.all()[request.data['params']['start']:request.data['params']['end']]
        for field in queryset:
            for im in PartsImg.objects.filter(parts__id=field.id)[:1]:
                field.f_img = im.img.url
                field.save()
        serializer_class = PartsSerializer(queryset, many=True)
        return Response(serializer_class.data)


class PartsImgViewSet(APIView):
    def post(self, request):
        print("REQUEST", request.data['params']['id'])
        queryset = PartsImg.objects.filter(parts__id=request.data['params']['id'])
        serializer_class = PartsImgSerializer(queryset, many=True)
        return Response(serializer_class.data)


class PartsOrderViewSet(APIView):
    def post(self, request):
        print(request.data['params'])
        order = OrderShop.objects.create(delivery_status=request.data['params']['type_delivery'], name=request.data['params']['name'], phone=request.data['params']['phone'], address=request.data['params']['adress'], total_price=request.data['params']['tp'])
        for item in request.data['params']['cart']:
            print(item['id'])
            ProductInOrder.objects.create(order=order, product_id=item['id'], count=item['count'], )
        send_mail(u'ВАЖНО! На сайте ТВ СЕРВИСА оформлена покупка на сумму'+str(request.data['params']['tp']), u'Номер заказа:'+str(order.id), settings.EMAIL_HOST_USER, ['skret002@mail.ru'])
        try:
            return Response({"status": "ok", "id": order.id})
        except Exception:
            return Response({"status": "bad", "id": order.id})
