from django.urls import path, include

from item.views import ItemOptionViewSet, ItemOptionImageViewSet, ItemOptionSizeViewSet
from .views import ShippingViewSet

# noinspection PyCallByClass,PyTypeChecker
shipping_list = ShippingViewSet.as_view({
    'post': 'create',
    'get': 'list'
})

# noinspection PyCallByClass,PyTypeChecker
shipping_detail = ShippingViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})


urlpatterns = [
    path('', shipping_list),
    path('<int:no>/', shipping_detail),
    # path('<int:no>/options', include(item_option_patterns)),
]

