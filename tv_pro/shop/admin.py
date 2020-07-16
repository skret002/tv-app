from django.contrib import admin
from .models import *
from nested_inline.admin import NestedModelAdmin, NestedTabularInline, NestedStackedInline
# Register your models here.

class ProductInOrderInline(admin.TabularInline):
    model = ProductInOrder
    extra = 0

class PartsImgInline(NestedStackedInline):
    model = PartsImg
    extra = 1


class PartsInline(NestedStackedInline):
    model = Parts
    extra = 0


class OrderShopAdmin(NestedModelAdmin):
    inlines = [
        ProductInOrderInline
    ]
    list_display = [field.name for field in OrderShop._meta.fields]

    class Meta:
        model = OrderShop

admin.site.register(OrderShop, OrderShopAdmin)



class PartsAdmin(NestedModelAdmin):
    exclude = ('f_img', 'order')
    inlines = [
        PartsImgInline,
        ]
    list_display = [field.name for field in Parts._meta.fields]

    class Meta:
        model = Parts


admin.site.register(Parts, PartsAdmin)


#class ProductInOrderAdmin (admin.ModelAdmin):
#    list_display = [field.name for field in ProductInOrder._meta.fields]
#
#    class Meta:
#        model = ProductInOrder
#
#admin.site.register(ProductInOrder, ProductInOrderAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Category._meta.fields]

    class Meta:
        model = Category

admin.site.register(Category, CategoryAdmin)


