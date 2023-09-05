from django.contrib import admin
from .models import Service,ServiceRequest
# Register your models here.




class ServiceAdmin(admin.ModelAdmin):
    list_display = ("id","title", "description","created_at")


class ServiceRequestAdmin(admin.ModelAdmin):
    list_display = ("id","user","service" ,"state")

admin.site.register(Service,ServiceAdmin)
admin.site.register(ServiceRequest,ServiceRequestAdmin)