from django.contrib import admin
from .models import newsletter

class listsub(admin.ModelAdmin):
    list_display= ('user_id','email')
    

    def has_add_permission(self, request):
        return False
admin.site.register(newsletter,listsub)