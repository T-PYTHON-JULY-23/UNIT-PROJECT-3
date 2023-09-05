from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Service(models.Model):
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=512)
    image = models.ImageField(upload_to="images/", default="images/default.jpg")
    created_at = models.DateTimeField(auto_now_add=True)

class ServiceRequest(models.Model):
    status_list = (("pending", "Pending"), ("in_progress", "In Progress"), ("done", "Done"), ("canceled", "Canceled"))

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=128, choices=status_list)