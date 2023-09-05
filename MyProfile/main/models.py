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
    status_choices = (('Pending', "Pending"), ('In_progress', "In_progress"), ('Done', "Done"), ('Canceled', "Canceled"),)

    service=models.ForeignKey(Service,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    status = models.CharField(choices=status_choices,default='Pending',max_length=12)


    def __str__(self) -> str:
        return f"{self.service.title} for {self.user.first_name}"
