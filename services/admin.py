from django.contrib import admin
from .models import vehicleInfo
from .models import Category
from .models import vehicleReview
from .models import bookInstantly
from .models import callBack


# Register your models here.
admin.site.register(vehicleInfo)
admin.site.register(Category)
admin.site.register(vehicleReview)
admin.site.register(bookInstantly)
admin.site.register(callBack)