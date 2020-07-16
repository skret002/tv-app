from django.urls import path
from rest_framework import routers
from .views import *
#
router = routers.DefaultRouter()
##router.register(r'type_lcd', TypeLcdViewSet)
#
## URLs настраиваются автоматически роутером
##urlpatterns = router.urls
#
urlpatterns = [
    path(r'shop_categoty/', CategoryViewSet.as_view()),
    path(r'shop_parts/', PartsViewSet.as_view()),
    path(r'shop_parts_img/', PartsImgViewSet.as_view()),
    path(r'shop_order/', PartsOrderViewSet.as_view()),

]+router.urls
