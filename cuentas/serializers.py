from rest_framework import serializers
from cuentas.models.product import Product

class Productserializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'title', 'description','product_category', 'price', 'available')
        read_only_fields = ('available', )
