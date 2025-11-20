from django.contrib import admin
from cars.models import Brand, Car


class BrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at',)
    search_fields = ('name',)


class CarAdmin(admin.ModelAdmin):
    list_display = ('id', 'model', 'brand_name', 'color',
                    'factory_year', 'model_year', 'created_at',)
    search_fields = ('model',)
    list_filter = ('brand',)

    def brand_name(self, obj):
        return obj.brand.name
    brand_name.admin_order_field = 'brand__name'
    brand_name.short_description = 'Brand'


admin.site.register(Brand, BrandAdmin)
admin.site.register(Car, CarAdmin)