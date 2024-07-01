from django.contrib import admin
from apps.product.models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'code', 'iva','number_iva','compare_valor',
                    'valor', 'quantity', 'sold', )
    list_display_links = ('id', 'name', )
    list_filter = ('category', )
    list_editable = ( 'iva','number_iva','compare_valor', 'valor', 'quantity', )
    search_fields = ('name', 'description', )
    list_per_page = 25

admin.site.register(Product, ProductAdmin)