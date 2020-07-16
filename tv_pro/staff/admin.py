from django.contrib import admin
from .models import *
from nested_inline.admin import NestedModelAdmin, NestedTabularInline, NestedStackedInline
# Register your models here.


class StaffInline(NestedStackedInline):
    model = Staff
    extra = 1


class AboutStaffAdmin(NestedModelAdmin):
    inlines = [
        StaffInline,
        ]
    list_display = [field.name for field in AboutStaff._meta.fields]

    class Meta:
        model = AboutStaff


admin.site.register(AboutStaff, AboutStaffAdmin)
