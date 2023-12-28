from django.db import models
from django.contrib.auth.models import User
from brand.models import Brand



class Car(models.Model):
    name = models.CharField(max_length=100)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    details = models.TextField()
    quantity = models.PositiveIntegerField(default=0)
    color = models.CharField(max_length=50)
    price = models.BigIntegerField()
    image = models.ImageField(upload_to ='uploads/', blank = True, null = True) 

    def __str__(self):
        return self.name

class Comment(models.Model):
    post = models.ForeignKey(Car, on_delete=models.CASCADE ,related_name="comments")
    name = models.CharField(max_length = 30)
    email = models.EmailField(unique=True)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f" comments by {self.name}"
    


class Purchase(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    purchase_date = models.DateTimeField(auto_now_add=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)