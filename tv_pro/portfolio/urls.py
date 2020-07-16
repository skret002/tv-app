from django.urls import path
from rest_framework import routers
from .views import PortfolioViewSet, PortfolioImgViewSet

router = routers.DefaultRouter()
#router.register(r'type_lcd', TypeLcdViewSet)

# URLs настраиваются автоматически роутером
#urlpatterns = router.urls

urlpatterns = [
    path(r'portfolio/', PortfolioViewSet.as_view()),
    path(r'portfolio_img/', PortfolioImgViewSet.as_view()),
]+router.urls
