from django.contrib import admin
from service.models import Service,ServiceRequest

# Register your models here.
class ServiceAdmin(admin.ModelAdmin):
    list_display=('title','created_at')
    list_filter=('created_at',)

class ServiceRequestAdmin(admin.ModelAdmin):
    list_display=('user','service','status','request_created_at','note')
    list_filter=('status',)


admin.site.register(Service,ServiceAdmin)
admin.site.register(ServiceRequest,ServiceRequestAdmin)

# Register your models here.
