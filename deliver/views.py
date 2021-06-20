from django.http import Http404
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import *
from account.models import *
from .serializers import *
from django.contrib.auth.models import User
from account.models import Client

#### Restaurant
class RestaurantList(generics.ListAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer


class RestaurantCreate(generics.CreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer


class RestaurantDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer


#### Meal
#### to get list of meals ( GET request) and create a new meal ( POST request)
class MealCreate(APIView):
    # queryset = Meal.objects.all()
    # serializer_class = MealSerializer
    def get_object_restaurant(self, pk):
        try:
            return Restaurant.objects.get(pk=pk)
        except Cart.DoesNotExist:
            raise Http404


    def get_object_category(self, pk):
        try:
            return Category.objects.get(pk=pk)
        except Cart.DoesNotExist:
            raise Http404

    def post(self, request, *args, **kwargs):
        data = request.data
        restaurant = self.get_object_restaurant(data["restaurant"])
        category = self.get_object_category(data["category"])
        meal = Meal.objects.create(name=data["name"], ingredients=data["ingredients"], price=data["price"],
                                   photo=data["photo"],restaurant = restaurant,category=category)

        serializer = MealSerializer(meal)
        return Response(serializer.data)



class MealListAll(generics.ListAPIView):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer

class MealList(generics.RetrieveAPIView):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer


### to search for a meal by ID of the restaurant
class MealSearch(APIView):

    def get_object(self, restaurant):
        try:
            return Meal.objects.filter(restaurant=restaurant)
        except Meal.DoesNotExist:
            raise Http404

    def get(self, request, restaurant, format=None):
        meal = self.get_object(restaurant)
        serializer = MealSerializer(meal, many=True)
        return Response(serializer.data)


class MealDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Meal.objects.all()
    serializer_class = MealSerializer


#### Category
class CategoryList(generics.ListCreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = CategorySerializer


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


#### Cart
class CartList(generics.ListAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

class CartAdd(APIView):

    def get_object(self, pk):
        try:
            return Meal.objects.get(pk=pk)
        except Cart.DoesNotExist:
            raise Http404

    def post(self, request, *args, **kwargs):
        data = request.data
        meal_obj = self.get_object(data["meal"])
        cart = Cart.objects.create()
        cart.meal.add(meal_obj)
        cart.restaurant.add(meal_obj.restaurant)
        cart.price = meal_obj.price
        client = Client.objects.get(pk=request.data["client"])
        cart.client = client
        serializer = CartSerializer(cart)
        return Response(serializer.data)

class AddMealToCart(APIView):##### add new meal to cart
    def get_object_meal(self, pk):
        try:
            return Meal.objects.get(pk=pk)
        except Cart.DoesNotExist:
            raise Http404

    def get_object(self, pk):
        try:
            return Cart.objects.get(pk=pk)
        except Cart.DoesNotExist:
            raise Http404



    def post(self, request, pk, fomart=None):
        cart = self.get_object(pk)
        meal_obj = self.get_object_meal(request.data["meal"])
        restaurant_obj = meal_obj.restaurant
        cart.meal.add(meal_obj)
        cart.restaurant.add(restaurant_obj)
        client = Client.objects.get(pk=request.data["client"])
        cart.client = client
        cart.save()
        serializer = CartSerializer(cart)
        return Response(serializer.data)


class deleteMealCart(APIView):##### add new meal to cart

    def get_object_meal(self, pk):
        try:
            return Meal.objects.get(pk=pk)
        except Cart.DoesNotExist:
            raise Http404

    def get_object(self, pk):
        try:
            return Cart.objects.get(pk=pk)
        except Cart.DoesNotExist:
            raise Http404

    def delete(self, request, pk, fomart=None):
        cart = self.get_object(pk)
        meal_obj = self.get_object_meal(request.data["meal"])
        restaurant_obj = meal_obj.restaurant
        cart.meal.remove(meal_obj)
        cart.restaurant.remove(restaurant_obj)
        client = Client.objects.get(pk=request.data["client"])
        cart.client = client
        cart.save()
        serializer = CartSerializer(cart)
        return Response(serializer.data)


class CartModifier(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

##### Orders

#### create a new Order

class OrderList(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderAdd(APIView):
    def get_object(self, pk):
        try:
            return Cart.objects.get(pk=pk)
        except Cart.DoesNotExist:
            raise Http404

    def post(self, request, *args, **kwargs):
        data = request.data
        cart = self.get_object(data["cart"])
        order = Order.objects.create()
        order.cart = cart
        order.restaurant.add(data["restaurant"])
        client = Client.objects.get(pk=request.data["client"])
        order.client = client
        order.status = data["status"]
        order.save()
        serializer = OrderSerializer(order)
        return Response(serializer.data)


### search for Order by Restaurant ID
class OrderSearch(APIView):
    def get_object(self, restaurant):
        try:
            return Order.objects.filter(restaurant=restaurant)
        except Order.DoesNotExist:
            raise Http404

    def get(self, request, restaurant, format=None):
        order = self.get_object(restaurant)
        serializer = OrderSerializer(order, many=True)
        return Response(serializer.data)


#### ### search for Order by Client_user ID
class OrderClientSearch(APIView):
    def get_object(self, client):
        try:
            return Order.objects.filter(client__user_id=client)
        except Order.DoesNotExist:
            raise Http404

    def get(self, request, client, format=None):
        order = self.get_object(client)
        serializer = OrderSerializer(order, many=True)
        return Response(serializer.data)