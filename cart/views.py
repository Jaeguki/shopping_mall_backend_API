from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from cart.models import Cart
from cart.serializers import CartSerializer


class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    lookup_field = 'no'
