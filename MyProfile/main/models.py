from django.db import models

# Create your models here.

class Service(models.Model):


    title = models.CharField(max_length=2048)
    description = models.TextField()
    image = models.ImageField(upload_to="images/", default="images/default.png")
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self) -> str:
        return f"{self.title}"