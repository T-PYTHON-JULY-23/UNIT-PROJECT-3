from django.db import models
from django.contrib.auth.models import User


class Service(models.Model):
    icon= models.TextField()
    title = models.CharField(max_length=2048)
    description = models.TextField()
    content= models.TextField()
    publish_date = models.DateField()
    image= models.ImageField(upload_to="images/",default="images/default.jpg")

class ServiceRequest (models.Model):
    category_status = (("pending", "pending"), ("in_progress", "in_progress"), ("done", "done"), ("canceled", "canceled"))
    status = models.CharField(max_length=2048)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)