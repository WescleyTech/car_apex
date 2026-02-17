from django.contrib import admin
from cars.models import Car, Brand, Fuel, Transmission

# Register your models here.

class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class FuelAdmin(admin.ModelAdmin):
    list_display = ('type',)
    search_fields = ('type',)

class TransmissionAdmin(admin.ModelAdmin):
    list_display = ('type',)
    search_fields = ('type',)

class CarAdmin(admin.ModelAdmin):
    list_display = ('model', 'brand', 'model_year', 'value',)
    search_fields = ('model', 'brand',)

admin.site.register(Brand, BrandAdmin)
admin.site.register(Fuel, FuelAdmin)
admin.site.register(Transmission, TransmissionAdmin)
admin.site.register(Car, CarAdmin)

