from django.contrib import admin
from .models import Service , Requests

# Register your models here.


class ServiceAdmin(admin.ModelAdmin):

    list_display = ("title", "description","created_at")
    list_filter = ("title", "created_at")
  

# Register your models here.
admin.site.register(Service , ServiceAdmin)



class requestsAdmin(admin.ModelAdmin):
    list_display = ("user", 'logo')

admin.site.register(Requests, requestsAdmin)
