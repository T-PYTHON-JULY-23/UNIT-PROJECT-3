from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Dessert(models.Model):
    
    title=models.CharField(max_length=256)
    ingredients=models.TextField()
    instructions=models.TextField(default="test")
    image=models.ImageField(upload_to="images/")
    created_at = models.DateTimeField(auto_now_add=True,blank=True)


class Order(models.Model):
    status_choices = (
               ('confirmed', 'confirmed'),
               ('completed', 'completed'),
               ('in progress','in progress'),
               ('Canceled','Canceled'))
    
    item = models.ForeignKey(Dessert, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    descrption=models.CharField(max_length = 100, choices = status_choices,default=None)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.first_name} on {self.item.title}"



class Confirm(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Dessert, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
