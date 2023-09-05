from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Service(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    
    created_at = models.DateTimeField(auto_now_add=True)
   

class ServiceRequest(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('done', 'Done'),
        ('canceled', 'Canceled'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
