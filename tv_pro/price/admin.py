from django.contrib import admin
from .models import *
from nested_inline.admin import NestedModelAdmin, NestedTabularInline, NestedStackedInline
# Register your models here.

admin.site.register(NameBrend)
admin.site.register(LogoTv)


class PriceInline(NestedStackedInline):
    model = TvSizePrice
    extra = 1


class MalfunksInline(NestedStackedInline):
    model = Malfunks
    inlines = [PriceInline, ]
    extra = 1

class TvBrendAdmin(admin.ModelAdmin):
    list_display = [field.name for field in TvBrend._meta.fields]

    class Meta:
        model = TvBrend

admin.site.register(TvBrend, TvBrendAdmin)


class TvSizePriceAdmin(admin.ModelAdmin):
    list_display = [field.name for field in TvSizePrice._meta.fields]

    class Meta:
        model = TvSizePrice


admin.site.register(TvSizePrice, TvSizePriceAdmin)


class TypeLcdAdmin(admin.ModelAdmin):
    list_display = [field.name for field in TypeLcd._meta.fields]

    class Meta:
        model = TypeLcd


admin.site.register(TypeLcd, TypeLcdAdmin)


class MalfunksAdmin(NestedModelAdmin):
    list_display = [field.name for field in Malfunks._meta.fields]
    inlines = [
        PriceInline,
    ]
    class Meta:
        model = Malfunks


admin.site.register(Malfunks, MalfunksAdmin)


class PriceAdmin(NestedModelAdmin):
    list_display = [field.name for field in Price._meta.fields]
    inlines = [
        MalfunksInline,
    ]
    class Meta:
        model = Price


admin.site.register(Price, PriceAdmin)
