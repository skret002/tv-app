from rest_framework import serializers
from .models import Home, SlideInHome, TypesOfMalfunctions, AboutInHome, InfoAboutOrder, Reviews

class HomeSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = Home
        fields="__all__"


class ReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = Reviews
        fields = "__all__"

class TypesOfMalfunctionsSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 4
        model = TypesOfMalfunctions
        fields = "__all__"


class AboutInHomeSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 0
        model = AboutInHome
        fields = "__all__"


class  InfoAboutOrderSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 0
        model = InfoAboutOrder
        fields = "__all__"
