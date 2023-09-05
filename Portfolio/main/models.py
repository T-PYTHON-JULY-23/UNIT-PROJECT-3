from django.db import models
from django.contrib.auth.models import User


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=512)
    subject = models.CharField(max_length=2048)
    message = models.CharField(max_length=2048)
    created_at = models.DateTimeField(auto_now_add=True)


