from django.urls import path, include

from .views import MallViewSet

# noinspection PyCallByClass,PyTypeChecker
mall_list = MallViewSet.as_view({
    'post': 'create',
    'get': 'list'
})

# noinspection PyCallByClass,PyTypeChecker
mall_detail = MallViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
urlpatterns = [
    path('', mall_list),
    path('<int:no>/', mall_detail),
    path('<int:no>/categories/', include('category.urls')),
]