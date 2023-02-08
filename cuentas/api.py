from rest_framework import viewsets, permissions
from cuentas.models.product import Product
from .serializers import Productserializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = Productserializer