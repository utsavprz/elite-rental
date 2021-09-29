from django.contrib import admin
from .models import vehicleInfo
from .models import Category
from .models import vehicleReview
from .models import bookInstantly
from .models import callBack
from .models import paymentGateway


# Register your models here.
admin.site.register(vehicleInfo)
admin.site.register(Category)
admin.site.register(vehicleReview)

class listBook(admin.ModelAdmin):
    list_display= ('id','user_id', 'car_id', 'number','pickAddress','pickDate','pickTime','dropAddress','dropDate','dropTime','status')
    

    list_filter = [
         "pickDate",
         "status"
    ]

    def has_add_permission(self, request):
        return False

admin.site.register(bookInstantly,listBook)

class listcallback(admin.ModelAdmin):
    list_display= ('id','user_id', 'car_id', 'number','pickAddress','pickDate','pickTime','dropAddress','dropDate','dropTime','status')
admin.site.register(callBack,listcallback)


class listPay(admin.ModelAdmin):
    list_display= ('id', 'user', 'car', 'book','status')

    list_filter = [
         "status"
    ]

    def has_add_permission(self, request):
        return False

admin.site.register(paymentGateway,listPay)