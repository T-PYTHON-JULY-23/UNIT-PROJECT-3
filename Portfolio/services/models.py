from django.db import models
from django.contrib.auth.models import User



class Service(models.Model):
    title = models.CharField(max_length=2048)
    description=models.TextField()
    image = models.ImageField(upload_to="images/", default="images/default.jpg")
    created_at = models.DateTimeField(auto_now_add=True)


class ServiceRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    status_choise = (("Pending", "Pending"), ("In progress", "In progress"), ("done", "done"), ("canceled", "canceled"),)
    status = models.CharField(max_length=300, choices=status_choise , default="Pending")
