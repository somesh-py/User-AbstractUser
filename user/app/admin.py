from django.contrib import admin
from .models import CustomUser
# Register your models here.

@admin.register((CustomUser))
class CustomerUser(admin.ModelAdmin):
    list_display=['id','is_superuser','first_name','last_name','is_staff','is_active','email','bio','address']