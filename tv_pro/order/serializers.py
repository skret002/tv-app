from rest_framework import serializers
from .models import Order


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = Order
        fields = "__all__"
