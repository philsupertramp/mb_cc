from django.urls import path, re_path
from rest_framework.urlpatterns import format_suffix_patterns
from order import views

urlpatterns = [
    path('orders/', views.OrderList.as_view(), name='orders-list'),
    re_path('orders/(?P<pk>[0-9]+)/', views.OrderDetail.as_view(), name='orders-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)