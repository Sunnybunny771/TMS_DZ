from django.contrib import admin
from .models import CarBrand, CarType, Engine, Car

# Register your models here.


class CarInline(admin.StackedInline):
    model = Car


class CarAdmin(admin.ModelAdmin):
    list_display = ('brand', 'type', 'engine', 'published')
    list_display_links = ('brand', 'type', 'engine', 'published')
    search_fields = ('brand', 'type', 'engine')
    list_filter = ('brand', 'type', 'engine')
    raw_id_fields = ('brand', 'engine')


class CarTypeAdmin(admin.ModelAdmin):
    list_display = ('type', 'transmission', 'wheel_drive')
    list_display_links = ('wheel_drive', 'transmission', 'type')
    search_fields = ('transmisson', 'type')
    list_filter = ('transmission', 'wheel_drive')
    inlines = [CarInline, ]


class EngineAdmin(admin.ModelAdmin):
    list_display = ('type', 'volume', 'horsepower', 'fuel')
    list_display_links = ('type', 'volume', 'horsepower', 'fuel')
    search_fields = ('type', 'volume', 'horsepower', 'fuel')
    list_filter = ('volume', 'horsepower', 'fuel')
    inlines = [CarInline, ]


admin.site.register(CarBrand)
admin.site.register(Engine, EngineAdmin)
admin.site.register(CarType, CarTypeAdmin)
admin.site.register(Car, CarAdmin)
