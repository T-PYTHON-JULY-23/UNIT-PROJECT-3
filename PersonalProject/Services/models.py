from django.db import models
from django.contrib.auth.models import User




class Service(models.Model):


    title = models.CharField(max_length=200)
    content = models.TextField()
    photo = models.ImageField(upload_to='Service/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
    


class ServiceRequest(models.Model):
    status_choices=(('pending','pending'),('in_progress','in_progress'),('Done','Done'),('canceled','canceled'))

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    status = models.TextField(choices=status_choices,default='pending')
    description=models.TextField()
    file=models.FileField(upload_to='',null=True)
    deadline=models.DateTimeField(null=True)


