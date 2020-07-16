from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('skret002/', admin.site.urls),
    path('', include('tv_backend.urls')),
    path('', include('price.urls')),
    path('', include('order.urls')),
    path('', include('footer.urls')),
    path('', include('staff.urls')),
    path('', include('portfolio.urls')),
    path('', include('shop.urls')),
    path('tinymce/', include('tinymce.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
