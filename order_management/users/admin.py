from django.contrib import admin

# Register your models here.
from .models import CustomUser

@admin.register(CustomUser)
class product_admin(admin.ModelAdmin):
    list_display = ('username','email','password','role','phone_number','address')
    search_fields = ('username',)
    list_filter = ('is_active',)