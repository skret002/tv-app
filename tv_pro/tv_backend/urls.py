from django.urls import path
from rest_framework import routers
from .views import HomeViewSet, MalfunctionsViewSet, AboutInHomeViewSet, InfoAboutOrderSerializerViewSet, ReviewsViewSet

router = routers.DefaultRouter()
router.register(r'home', HomeViewSet)
router.register(r'malfunctions', MalfunctionsViewSet)
router.register(r'about_in_home', AboutInHomeViewSet)
router.register(r'about_order_block_in_home', InfoAboutOrderSerializerViewSet)
router.register(r'reviews', ReviewsViewSet)


# URLs настраиваются автоматически роутером
urlpatterns = router.urls
MalfunctionsViewSet
