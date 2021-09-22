from django.contrib import admin
from .models import vehicleInfo
from .models import Category

# Register your models here.
admin.site.register(vehicleInfo)
admin.site.register(Category)