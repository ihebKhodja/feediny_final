from django.db import models
from django.db.models import ForeignKey

from account.models import Client, Manager
from cloudinary.models import CloudinaryField

class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=512)
    rating = models.IntegerField()
    photo = models.CharField(max_length=255,blank=True)
    description = models.TextField(blank=True)
    lat = models.FloatField(blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)
    manager = models.ForeignKey('account.Manager', on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Meal(models.Model):
    name = models.CharField(max_length=255)
    photo = models.CharField(max_length=255,blank=True)
    ingredients = models.TextField(blank=True)
    price = models.FloatField()
    restaurant = models.ForeignKey('Restaurant', on_delete=models.CASCADE, blank=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, blank=True)
    order = models.ForeignKey('Order', on_delete=models.CASCADE, blank=True, null=True)


    def __str__(self):
        return self.name


class Cart(models.Model):
    restaurant = models.ManyToManyField('Restaurant')
    client = models.ForeignKey('account.Client', on_delete=models.CASCADE, null=True)
    price = models.FloatField(blank=True, null=True)
    meal = models.ManyToManyField('Meal')



    def __str__(self):
        return self.pk

class Order(models.Model):
    CHOICES = (
        ('DL', 'delivered'),
        ('PN', 'pending'),
        ('AC', 'accepted'),
        ('RF', 'refused'),
    )
    date = models.DateField(auto_now=False, auto_now_add=True)
    restaurant = models.ManyToManyField('Restaurant', blank=True)
    client = models.ForeignKey('account.Client',on_delete=models.CASCADE, null=True)
    cart = models.ForeignKey('Cart', on_delete=models.PROTECT, null=True)
    status = models.CharField(max_length=100, choices= CHOICES, null=True)

    def __str__(self):
        return self.pk