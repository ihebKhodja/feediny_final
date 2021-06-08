from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
# from account.models import Manager, Client

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


class ClientSerializer(serializers.ModelSerializer):
    # client= Client(user=user, email= email, username= username)
    # class Meta:
    #     model = Client
    #     fileds = ['user.email', 'user.username','user.password']
    #     extra_kwargs = {
    #         'password': {'write_only': True}
    #     },
    #
    #     def save(self):
    #         client = Client(
    #             email=self.validated_data['user.email'],
    #             username=self.validated_data['user.username'],
    #         )
    #         password=self.validated_data['user.password']
    #         client.set_password(password)
    #         client.save()
    #         return client
    pass