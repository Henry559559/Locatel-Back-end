from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
              'id',
            'name',
            'code',
            'photo',
            'descripcion',
            'iva',
            'number_iva',
            'valor',
            'compare_valor',
            'category',
            'quantity',
            'sold',
            'date_created',
            'get_thumbnail'
        ]



      