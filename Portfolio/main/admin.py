from django.contrib import admin
from .models import Comment
# Register your models here.
admin.site.register(Comment)
class commentAdmin(admin.ModelAdmin):
    list_display = ("id", 'subject')