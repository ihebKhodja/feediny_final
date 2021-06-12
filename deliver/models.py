from django.db import models
from account.models import Client, Manager


class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=512)
    rating = models.IntegerField()
    photo = models.ImageField(upload_to='photos/',blank=True)
    description = models.TextField(blank=True)
    lat = models.FloatField(blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)


    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Meal(models.Model):
    name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='photos/',blank=True)
    ingredients = models.TextField()
    price = models.FloatField()
    restaurant = models.ForeignKey('Restaurant', on_delete=models.CASCADE, blank=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, blank=True)
    order = models.ForeignKey('Order', on_delete=models.CASCADE, blank=True, null=True)


    def __str__(self):
        return self.name



class Cart(models.Model):
    restaurant = models.ForeignKey('Restaurant', on_delete=models.CASCADE, null=True)
    client = models.ForeignKey('account.Client', on_delete=models.CASCADE, null=True)
    price = models.IntegerField()
    meal = models.ManyToManyField('Meal')


class Order(models.Model):
    CHOICES = (
        ('DL', 'delivered'),
        ('PN', 'pending'),
        ('AC', 'accepted'),
        ('RF', 'refused'),
    )
    date = models.DateTimeField(auto_now=False, auto_now_add=False)
    state = models.CharField(max_length=100)
    restaurant = models.ManyToManyField('Restaurant')
    client = models.ForeignKey('account.Client', on_delete=models.PROTECT, null=True)
    cart = models.ForeignKey('Cart', on_delete=models.PROTECT, null=True)
    status = models.CharField(max_length=100, choices= CHOICES, null=True)