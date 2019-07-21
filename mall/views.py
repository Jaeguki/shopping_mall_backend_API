from rest_framework import viewsets
from .models import Mall
from .serializers import MallSerializer


class MallViewSet(viewsets.ModelViewSet):
    queryset = Mall.objects.all()
    serializer_class = MallSerializer
    lookup_field = 'no'


