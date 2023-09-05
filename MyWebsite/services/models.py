from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Service (models.Model):
  
  title=models.CharField(max_length=2048)
  description=models.TextField()
  image=models.ImageField(upload_to="images/", default="images/default.jpeg")
  created_at=models.DateTimeField(auto_now_add=True)

 
  def __str__(self) -> str:
    return f"{self.title}"



class Requests (models.Model):
    status_choices=(("pending", "pending"), ("in_progress", "in_progress"), ("done", "done"), ("canceled", "canceled"), )
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    logo = models.ForeignKey(Service, on_delete=models.CASCADE)

    status =models.TextField(choices=status_choices,default="pending")

