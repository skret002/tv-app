from django.urls import path
from rest_framework import routers
from .views import StaffViewSet, SaleInFooterViewSet, CenterInFooterViewSet

router = routers.DefaultRouter()
urlpatterns = [
    path(r'footer_staff/', StaffViewSet.as_view()),
    path(r'sale_in_footer/', SaleInFooterViewSet.as_view()),
    path(r'content_in_footer/', CenterInFooterViewSet.as_view()),
]+router.urls
