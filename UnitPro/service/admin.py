from django.contrib import admin
from .models import Service,ServiceRequest,Comment

# Register your models here.
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at")


class ServiceRequestAdmin(admin.ModelAdmin):
    list_display = ("user", 'service', 'status')


class CommentAdmin(admin.ModelAdmin):
    list_display = ("user", 'service', 'rating')
   

admin.site.register(Service, ServiceAdmin)
admin.site.register(ServiceRequest, ServiceRequestAdmin)
admin.site.register(Comment, CommentAdmin)

   