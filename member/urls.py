from django.urls import path, include

from .views import MemberViewSet

# noinspection PyCallByClass,PyTypeChecker
member_list = MemberViewSet.as_view({
    'post': 'create',
    'get': 'list'
})

# noinspection PyCallByClass,PyTypeChecker
member_detail = MemberViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
urlpatterns = [
    path('', member_list),
    path('<int:no>/', member_detail),
    path('<int:no>/malls/', include('mall.urls')),
]