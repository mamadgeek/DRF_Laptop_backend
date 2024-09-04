from django.urls import path , include
# from .views_api_products import showing_laptops ,laptop_detail
# from .views_api_products import showing_laptops ,laptop_detail
from .views import Laptpsviewset ,UsersView,CpuView,RamView,GpuView
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
router=DefaultRouter()
router.register(r'laptops',Laptpsviewset,basename='laptops')

urlpatterns=[
    path('',include(router.urls)) ,
    path('users/',UsersView.as_view(),name='users_urls'),
    path('ram/',RamView.as_view(),name='ram_urls'),
    path('gpu/',GpuView.as_view(),name='gpu_urls'),
    path('cpu/',CpuView.as_view(),name='cpu_urls'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('showing_laptops/',showing_laptops.as_view(),name='show_all_laptops'),
    # path('<int:pk>/',laptop_detail.as_view(),name='show_an_laptop')
] 



