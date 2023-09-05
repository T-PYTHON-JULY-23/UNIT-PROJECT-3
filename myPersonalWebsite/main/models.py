from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Service(models.Model):

    title = models.CharField(max_length=2048)
    description = models.TextField()
    image = models.ImageField(upload_to="images/")
    publish_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.title}"
    
class ServiceRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    status= models.CharField(max_length=2048)
    def __str__(self):
        return f"{self.service.title}"