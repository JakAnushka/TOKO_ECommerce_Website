from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.
class Categories(models.Model):
    image=models.ImageField(upload_to="categories/product_img")
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=200)


class Contact(models.Model):
    name=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    phone=models.CharField(max_length=12)
    desc=models.TextField()
    date=models.DateField()

    def __str__(self):
        return self.name




class Product(models.Model):
    Availability=(('In Stock','In Stock'),('Out of Stock','Out of Stock'))
    image=models.ImageField(upload_to="toko/product_img")
    name=models.CharField(max_length=100)
    price=models.IntegerField()
    availability=models.CharField(choices=Availability,null=True,max_length=100)
    date=models.DateField(auto_now_add=True)


    def __str__(self):
        return self.name


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    address=models.TextField()
    town = models.TextField()
    addresstype=models.TextField()
    state=models.TextField()
    mobile=models.CharField(max_length=11)
    pincode=models.CharField(max_length=10)
    payment = models.CharField(max_length=200)
    paid=models.BooleanField(default=False,null=True)
    date=models.DateField(default=datetime.datetime.today)




class OrderItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to="toko/order_img")
    product=models.CharField(max_length=200)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity=models.CharField(max_length=5)
    price=models.IntegerField()

