from django.urls import path, include

from non_member.views import NonMemberViewSet

non_member_list = NonMemberViewSet.as_view({
    'post': 'create',
    'get': 'list'
})

order_detail = NonMemberViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
urlpatterns = [
    path('', non_member_list),
    path('<int:no>/', non_member_list),
    path('<int:no>/carts/', include('cart.urls')),
    path('<int:no>/shippings/', include('shipping.urls')),
]