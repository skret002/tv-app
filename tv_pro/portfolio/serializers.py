from rest_framework import serializers
from .models import Portfolio, PortfolioImg


class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = Portfolio
        fields = "__all__"


class PortfolioImgSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = PortfolioImg
        fields = "__all__"
