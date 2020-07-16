from rest_framework import serializers
from .models import Staff


class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 2
        model = Staff
        fields = "__all__"
