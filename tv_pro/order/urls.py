from django.urls import path
from rest_framework import routers
from .views import OrderViewSet

router = routers.DefaultRouter()
urlpatterns = [
    path(r'order/', OrderViewSet.as_view()),
]+router.urls
