from rest_framework import serializers
from .models import *


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = Category
        fields = "__all__"


class PartsSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 3
        model = Parts
        fields = "__all__"


class PartsImgSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 3
        model = PartsImg
        fields = "__all__"
