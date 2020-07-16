from rest_framework import serializers
from .models import Price, TypeLcd, TvBrend, Malfunks, TvSizePrice



class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 6
        model = Price
        fields = ['id', 'brend_size']


class TvSizePriceSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = TvSizePrice
        fields = ['id', 'size', 'price', 'malfunk']

class TypeLcdSerializer(serializers.ModelSerializer):

    class Meta:
        depth = 1
        model = TypeLcd
        fields = ['id', 'type_lcd', 'type_lcd_img']
