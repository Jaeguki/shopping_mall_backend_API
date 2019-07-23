from django.urls import path, include

from item.views import ItemOptionViewSet, ItemOptionImageViewSet, ItemOptionSizeViewSet
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

item_option_list = ItemOptionViewSet.as_view({
    'post': 'create',
    'get': 'list'
})

# noinspection PyCallByClass,PyTypeChecker
item_option_detail = ItemOptionViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

item_option_image_list = ItemOptionImageViewSet.as_view({
    'post': 'create',
    'get': 'list'
})

# noinspection PyCallByClass,PyTypeChecker
item_option_image_detail = ItemOptionImageViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

item_option_size_list = ItemOptionSizeViewSet.as_view({
    'post': 'create',
    'get': 'list'
})

# noinspection PyCallByClass,PyTypeChecker
item_option_size_detail = ItemOptionSizeViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

item_option_image_patterns = [
    path('', item_option_image_list),
    path('<int:no>/', item_option_image_detail),
]

item_option_size_patterns =[
    path('', item_option_size_list),
    path('<int:no>/', item_option_size_detail),
]

item_option_patterns = [
    path('', item_option_list),
    path('<int:no>/', item_option_detail),
    path('<int:no>/sizes/', include(item_option_size_patterns)),
    path('<int:no>/images/', include(item_option_image_patterns)),

]

urlpatterns = [
    path('', item_list),
    path('<int:no>/', item_detail),
    path('<int:no>/options', include(item_option_patterns)),
]

