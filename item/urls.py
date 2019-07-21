from django.urls import path, include

from .views import ItemViewSet

# noinspection PyCallByClass,PyTypeChecker
item_list = ItemViewSet.as_view({
    'post': 'create',
    'get': 'list'
})

# noinspection PyCallByClass,PyTypeChecker
item_detail = ItemViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
urlpatterns = [
    path('', item_list),
    path('<int:no>/', item_detail),
    # path('<int:no>/categories/', include('category.urls')),
]