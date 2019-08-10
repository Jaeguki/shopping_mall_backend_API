from django.forms import model_to_dict
from django.http import JsonResponse
from rest_framework import viewsets
from .models import Mall
from .serializers import MallSerializer


class MallViewSet(viewsets.ModelViewSet):
    queryset = Mall.objects.all()
    serializer_class = MallSerializer
    lookup_field = 'no'
