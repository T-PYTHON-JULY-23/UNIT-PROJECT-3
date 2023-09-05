from django.contrib import admin
from .models import Shirt, Comment

# Register your models here.


class ShirtAdmin(admin.ModelAdmin):

    list_display = ("title", "price")
    #list_filter = ("title", "publish_date")


class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'shirt', 'rating')
   # list_filter = ('post', "rating")

admin.site.register(Shirt, ShirtAdmin)
admin.site.register(Comment, CommentAdmin)
