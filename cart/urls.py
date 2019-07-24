from django.urls import path, include

from .views import CartViewSet

# noinspection PyCallByClass,PyTypeChecker
category_list = CartViewSet.as_view({
    'post': 'create',
    'get': 'list'
})

# noinspection PyCallByClass,PyTypeChecker
category_detail = CartViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
urlpatterns = [
    path('', category_list),
    path('<int:no>/', category_detail),
    path('<int:no>/items/', include('item.urls')),
]