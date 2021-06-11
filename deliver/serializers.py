from rest_framework import serializers, permissions
from .models import *
from django.contrib.auth.models import User
from account.models import Manager, Client



class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['id','name', 'address','rating', 'photo', 'description', 'lat', 'lng']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','name']


class MealSerializer(serializers.ModelSerializer):
    restaurant = RestaurantSerializer()
    category = CategorySerializer()
    #owner = serializers.ReadOnlyField(source='owner.phone_number')

    class Meta:
        model = Meal
        fields = ['id','name','photo','ingredients', 'price', 'restaurant', 'category']


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id','date', 'state', 'meal']

##### user Manager
# class ManagerSerializer(serializers.ModelSerializer):
#     meals = serializers.PrimaryKeyRelatedField(many= True, queryset= Meal.objects.all())
#
#     class Meta:
#         model = Manager
#         fields = ['user.id','user.username','meals']


class CartSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cart
        fields = ['id','restaurant','price','meal']

