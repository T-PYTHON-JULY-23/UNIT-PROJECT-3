from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Service(models.Model):
    title = models.CharField(max_length=2048)
    description = models.TextField()
    image = models.ImageField(upload_to="images/", default="images/default.jpg")
    created_at = models.DateField(auto_now_add=True)


class ServiceRequest(models.Model):
    choices= (("pending",'pendin'),("in_progress","in_progress"),("done","done"), ("canceled","canceled"))
    
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status=models.CharField(max_length=120, choices=choices,default="pending" )
    def __str__(self):
        return f"{self.user.first_name} on {self.service.title}"
