from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Service(models.Model):


    title = models.CharField(max_length=2048)
    description = models.TextField()
    image = models.ImageField(upload_to="images/", default="images/default.png")
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self) -> str:
        return f"{self.title}"
    
class ServiceRequest(models.Model):
    status_choices = ((1, "pending"), (2, "in_progress"), (3, "done"), (4, "canceled"),)

    service=models.ForeignKey(Service,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    status = models.IntegerField(choices=status_choices,default=1)


    def __str__(self) -> str:
        return f"{self.service.title} for {self.user.first_name}"
