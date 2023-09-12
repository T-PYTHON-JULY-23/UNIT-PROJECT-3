from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Service(models.Model):

    service_choices = (('Manicures', 'Manicures'), ('Pedicures', 'Pedicures'), ('Nail design', 'Nail design'),)

    title  =  models.CharField(max_length=128, choices= service_choices)
    description = models.TextField()
    image = models.ImageField(upload_to="images/")
    created_at = models.DateField(auto_now=True)


class ServiceRequest(models.Model):

    status_choices= (('pending','pending'),('in_progress','in_progress'),('done','done'),('canceled','canceled'),)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.TextField( choices= status_choices,default='pending')




class Comment(models.Model):

    rating_choices = ((1, "1 Star"), (2, "2 Star"), (3, "3 Star"), (4, "4 Star"), (5, "5 Star"), )

    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    rating = models.IntegerField(choices=rating_choices)
    review = models.DateTimeField(auto_now_add=True)