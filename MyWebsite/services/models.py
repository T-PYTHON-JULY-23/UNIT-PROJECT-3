from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Service(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    image = models.ImageField(upload_to="img/", default="img/default.jpeg")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.title}"



class ServiceRequest(models.Model):
    state_choices = (("pending","Pending"),("in_progress","In Progress"),("done","done"),("canceled","Canceled"))
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    state = models.CharField(max_length=300 ,choices=state_choices, default="pending")

