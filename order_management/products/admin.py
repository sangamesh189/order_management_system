from django.contrib import admin

# Register your models here.
from .models import product

@admin.register(product)
class product_admin(admin.ModelAdmin):
    list_display = ('name','price','stock','is_active')
    search_fields = ('name',)
    list_filter = ('is_active',)