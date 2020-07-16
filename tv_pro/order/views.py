from django.shortcuts import render
from .models import Order
from .serializers import OrderSerializer
from rest_framework import generics, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from time import gmtime, strftime
from django.core.mail import send_mail
from django.conf import settings
import telebot
import requests

# Create your views here.


class OrderViewSet(APIView):
    def post(self, request):
        #bot = telebot.TeleBot('1121575725:AAHRJSUPUr_-NfO-x0EJ0wiHfp2jkq2xbYg')
        #bot.send_message('@skret002', "Привет")
        time=""
        type_order = request.data["params"]["data"]["data"][0]["type"]
        name = request.data["params"]["data"]["data"][0]["name"]
        phone = request.data["params"]["data"]["data"][0]["phone"]
        if request.data["params"]["data"]["data"][0]["time"]:
            time = request.data["params"]["data"]["data"][0]["time"]
        else:
            time = str(int(strftime("%H:%M", gmtime())[:2])+3)+":"+str(int(strftime("%H:%M", gmtime())[3:5]))
        order_mes = str("Тип заказа:  " + type_order + "\n" + "Имя:  " + name + "\n"+
                        "Номер:  " + phone + "\n"+ "Звонить в " + time)
        if phone in [i.phone_number for i in Order.objects.all()]:
             return Response(u"order_have")
        else:
            pass
            try:
                Order.objects.create(type_order=type_order,
                                                    name=name,
                                                    time_call=time,
                                                    phone_number=phone)
                send_mail(u'НОВЫЙ ЗАКАЗ! На сайте ТВ СЕРВИСА новый заказ', order_mes, settings.EMAIL_HOST_USER, ['skret002@mail.ru'])
                return Response(u"true")
            except None:
                send_mail(u'НОВЫЙ ЗАКАЗ! На сайте ТВ СЕРВИСА новый заказ', "Произошла ошибка при заказе на сайте", settings.EMAIL_HOST_USER, ['skret002@mail.ru'])
                return Response(u"false")
