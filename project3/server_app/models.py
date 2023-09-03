from django.db import models
from django.contrib.auth.models import User

class ServerApp(models.Model):

    title = models.CharField(max_length=2048)
    description = models.TextField()
    image = models.ImageField(upload_to="images/", default="images/default.jpg")
    created_at = models.DateTimeField(auto_now_add=True)


# Create your models here.
class UserRequest (models.Model):
    category_choices = (("pending", "pending"), ("in_progress", "in_progress"), (" done","done "), ("canceled", "canceled"))

    user=models.ForeignKey(User, on_delete=models.CASCADE)
    ServerApp=models.ForeignKey(ServerApp, on_delete=models.CASCADE)
    status=models.CharField(max_length=2048,default="Pending", choices=category_choices)