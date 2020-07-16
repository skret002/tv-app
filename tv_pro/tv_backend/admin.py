from django.contrib import admin
from .models import *
# Register your models here.


class HomeAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Home._meta.fields]

    class Meta:
        model = Home

admin.site.register(Home, HomeAdmin)


class SlideInHomeAdmin(admin.ModelAdmin):
    list_display = [field.name for field in SlideInHome._meta.fields]

admin.site.register(SlideInHome, SlideInHomeAdmin)


class PagesAboutOfMalfunctionsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in PagesAboutOfMalfunctions._meta.fields]

admin.site.register(PagesAboutOfMalfunctions, PagesAboutOfMalfunctionsAdmin)


class TypesOfMalfunctionsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in TypesOfMalfunctions._meta.fields]

admin.site.register(TypesOfMalfunctions, TypesOfMalfunctionsAdmin)


class AboutInHomeAdmin(admin.ModelAdmin):
    list_display = [field.name for field in AboutInHome._meta.fields]

admin.site.register(AboutInHome, AboutInHomeAdmin)


class InfoAboutOrderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in InfoAboutOrder._meta.fields]


admin.site.register(InfoAboutOrder, InfoAboutOrderAdmin)


class ReviewsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Reviews._meta.fields]


admin.site.register(Reviews, ReviewsAdmin)
