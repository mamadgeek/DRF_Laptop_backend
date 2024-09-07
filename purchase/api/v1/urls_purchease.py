from django.urls import path ,  include
from rest_framework.routers import DefaultRouter
from .views_purchase import CartItemView ,  OrderView
routers_obj=DefaultRouter()
routers_obj.register(r'cart_item',CartItemView , basename='cart')
routers_obj.register(r'order',OrderView , basename='order')

urlpatterns=[
    path('',include(routers_obj.urls))
]

