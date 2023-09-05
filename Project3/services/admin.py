from django.contrib import admin
from .models import ServerApp, UserRequest

# Register your models here.

admin.site.register(ServerApp)
admin.site.register(UserRequest)

