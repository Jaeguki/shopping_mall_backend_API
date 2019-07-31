from django.urls import path

from .views import CartViewSet

# noinspection PyCallByClass,PyTypeChecker
cart_list = CartViewSet.as_view({
    'post': 'create',
    'get': 'list'
})

# noinspection PyCallByClass,PyTypeChecker
cart_detail = CartViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = [
    path('', cart_list),
    path('<int:no>/', cart_detail),
]