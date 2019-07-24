from django.urls import path, include

from order.views import OrderViewSet
from .views import MemberViewSet

# noinspection PyCallByClass,PyTypeChecker
order_list = OrderViewSet.as_view({
    'post': 'create',
    'get': 'list'
})

# noinspection PyCallByClass,PyTypeChecker
order_detail = OrderViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
urlpatterns = [
    path('', order_list),
    path('<int:no>/', order_detail),
    # path('<int:no>/orderItems/', include('order_item.urls')),
]