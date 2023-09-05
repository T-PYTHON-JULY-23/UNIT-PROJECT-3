from django.contrib import admin
from .models import Service ,ServiceRequest
# Register your models here.

class ServiceAdmine(admin.ModelAdmin):
    list_display = ("title", "description", "created_at")

admin.site.register(Service,ServiceAdmine)

class ServiceRequestAdmin(admin.ModelAdmin):
    list_display=("service","user","status")

admin.site.register(ServiceRequest,ServiceRequestAdmin)