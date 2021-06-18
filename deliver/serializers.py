from rest_framework import serializers, permissions

from account.serializers import ClientSerializer
from .models import *
from django.contrib.auth.models import User
from account.models import Manager, Client


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['id', 'name', 'address', 'rating', 'photo', 'description', 'lat', 'lng','manager']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class MealSerializer(serializers.ModelSerializer):
    restaurant = RestaurantSerializer()
    category = CategorySerializer()

    class Meta:
        model = Meal
        fields = ['id', 'name', 'photo', 'ingredients', 'price', 'restaurant', 'category']


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['id', 'restaurant', 'price', 'meal','client']



class OrderSerializer(serializers.ModelSerializer):
    client= ClientSerializer()

    class Meta:
        model = Order
        fields = ['id', 'date','restaurant', 'client', 'cart', 'status']


