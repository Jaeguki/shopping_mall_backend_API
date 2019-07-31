from django.urls import path

# noinspection PyCallByClass,PyTypeChecker
from order_item.views import OrderItemViewSet

order_item_list = OrderItemViewSet.as_view({
    'post': 'create',
    'get': 'list'
})

# noinspection PyCallByClass,PyTypeChecker
order_item_detail = OrderItemViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
urlpatterns = [
    path('', order_item_list),
    path('<int:no>/', order_item_detail),
]