from django.contrib import admin
from .models import *
# Register your models here.


class CenterInFooterAdmin(admin.ModelAdmin):
    list_display = [field.name for field in CenterInFooter._meta.fields]

    class Meta:
        model = CenterInFooter


admin.site.register(CenterInFooter, CenterInFooterAdmin)


class SaleInFooterAdmin(admin.ModelAdmin):
    list_display = [field.name for field in SaleInFooter._meta.fields]

    class Meta:
        model = SaleInFooter


admin.site.register(SaleInFooter, SaleInFooterAdmin)


class AdditionalStaffAdmin(admin.ModelAdmin):
    list_display = [field.name for field in AdditionalStaff._meta.fields]

    class Meta:
        model = AdditionalStaff


admin.site.register(AdditionalStaff, AdditionalStaffAdmin)
