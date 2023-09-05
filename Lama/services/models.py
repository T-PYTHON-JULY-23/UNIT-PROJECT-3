from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Service(models.Model):
    title= models.CharField(max_length=256)
    description=models.TextField()
    image = models.ImageField(upload_to="images/")
    created_at = models.DateField()


class ServiceRequest (models.Model):
    status_choices = (
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('done', 'Done'),
        ('canceled', 'Canceled'),
    )
    service=models.ForeignKey(Service,on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=20,choices=status_choices,default='pending')

    

