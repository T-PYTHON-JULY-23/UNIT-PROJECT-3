from django.db import models
from django.contrib.auth.models import User
from datetime import datetime



# Create your models here.



class Service(models.Model):
    category_choices = (("consultation", "consultation"), ("training", "training"), ("making activities", "making activities"), ("phone reapire", "phone reapire"))
    title = models.CharField(max_length=512)
    description = models.TextField()
    category = models.CharField(max_length=256, choices=category_choices)
    image = models.ImageField(upload_to="images")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.title}"


class ServiceRequest(models.Model):

    service_status=(('pending','pending'),('in_progress','in_progress'),('done','done'),('canceled','canceled'))
    


    service = models.ForeignKey(Service,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    pro_discription = models.TextField()
    status = models.CharField(max_length=256,choices=service_status,default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.service,self.user}"
    




