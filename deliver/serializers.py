from rest_framework import serializers, permissions
from .models import *
from django.contrib.auth.models import User
from account.models import Manager, Client


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['id', 'name', 'address', 'rating', 'photo', 'description', 'lat', 'lng']


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
    meal = MealSerializer(data=Meal.pk)
    class Meta:
        model = Cart
        fields = ['id', 'restaurant', 'price', 'meal']


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'date','restaurant', 'client', 'cart', 'status']


