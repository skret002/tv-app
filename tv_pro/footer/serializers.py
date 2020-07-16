from rest_framework import serializers
from .models import *


class AdditionalStaffSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = AdditionalStaff
        fields = "__all__"


class SaleInFooterSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = SaleInFooter
        fields = "__all__"


class CenterInFooterSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = CenterInFooter
        fields = "__all__"
