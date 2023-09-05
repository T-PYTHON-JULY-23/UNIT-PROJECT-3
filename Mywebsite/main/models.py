from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Shirt(models.Model):
    title = models.CharField(max_length=2048)
    price  = models.TextField()
    image = models.ImageField(upload_to="images/", default="images/default.jpg")

    def __str__(self) -> str:
        return f"{self.title}"

class ChildrenShirt(models.Model):
    title = models.CharField(max_length=2048)
    price  = models.TextField()
    image = models.ImageField(upload_to="images/", default="images/default.jpg")

    def __str__(self) -> str:
        return f"{self.title}"

class Comment(models.Model):

    rating_choices = ((1, "1 Star"), (2, "2 Star"), (3, "3 Star"), (4, "4 Star"), (5, "5 Star"), )

    shirt = models.ForeignKey(Shirt, on_delete=models.CASCADE)
    child_shirt=models.ForeignKey(ChildrenShirt,on_delete=models.CASCADE)
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    rating = models.IntegerField(choices=rating_choices)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.first_name} on {self.shirt.title}"
    

class Product(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    shirt= models.ForeignKey(Shirt, on_delete=models.CASCADE, null=True)
    child_shirt=models.ForeignKey(ChildrenShirt, on_delete=models.CASCADE, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
