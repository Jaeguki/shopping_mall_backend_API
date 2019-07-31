from rest_framework import viewsets
from shipping.models import Shipping
from shipping.serializers import ShippingSerializer


class ShippingViewSet(viewsets.ModelViewSet):
    queryset = Shipping.objects.all()
    serializer_class = ShippingSerializer
    lookup_field = 'no'
