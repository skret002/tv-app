from django.contrib import admin
from .models import *
from nested_inline.admin import NestedModelAdmin, NestedTabularInline, NestedStackedInline
# Register your models here.


class PortfolioImgInline(NestedStackedInline):
    model = PortfolioImg
    extra = 1


class PortfolioAdmin(NestedModelAdmin):
    inlines = [
        PortfolioImgInline,
        ]
    list_display = [field.name for field in Portfolio._meta.fields]

    class Meta:
        model = Portfolio


admin.site.register(Portfolio, PortfolioAdmin)
