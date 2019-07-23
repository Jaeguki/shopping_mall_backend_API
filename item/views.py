from rest_framework import viewsets
from .models import Item
from .serializers import ItemSerializer
from .serializers import ItemOptionSerializer
from .serializers import ItemOptionImageSerializer
from .serializers import ItemOptionSizeSerializer


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    # lookup_field = 'no'


class ItemOptionViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemOptionSerializer
    # lookup_field = 'no'


class ItemOptionImageViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemOptionImageSerializer
    # lookup_field = 'no'


class ItemOptionSizeViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemOptionSizeSerializer
    # lookup_field = 'no'
