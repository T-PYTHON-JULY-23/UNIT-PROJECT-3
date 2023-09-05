from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=512)
    description = models.CharField(max_length=2048)
    image = models.ImageField(upload_to="images/", default="images/default.jpg")
    start_date = models.DateField()
    end_date = models.DateField(default=None)
