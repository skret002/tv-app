from django.urls import path
from rest_framework import routers
from .views import StaffViewSet

router = routers.DefaultRouter()
#router.register(r'type_lcd', TypeLcdViewSet)

# URLs настраиваются автоматически роутером
#urlpatterns = router.urls

urlpatterns = [
    path(r'staff/', StaffViewSet.as_view()),
   # path(r'get_mulfunk/', MulfunkViewSet.as_view()),
]+router.urls
