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


#### Restaurant
class RestaurantList(generics.ListCreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer


class RestaurantDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer


#### Meal
#### to get list of meals ( GET request) and create a new meal ( POST request)
class MealCreate(generics.ListCreateAPIView):
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

class CartAdd(generics.CreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class AddMealToCart(APIView):##### add new meal to cart

    def get_object(self, pk):
        try:
            return Cart.objects.get(pk=pk)
        except Cart.DoesNotExist:
            raise Http404


    def post(self, request, pk, fomart=None):
        cart = self.get_object(pk)
        meal_obj = Meal.objects.get(id=request.data["meal"])
        cart.meal.add(meal_obj)
        cart.save()
        serializer = CartSerializer(cart)
        # if serializer.is_valid():
        #     serializer.save()
        return Response(serializer.data)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class deleteMealCart(APIView):##### add new meal to cart

    def get_object(self, pk):
        try:
            return Cart.objects.get(pk=pk)
        except Cart.DoesNotExist:
            raise Http404

    def delete(self, request, pk, fomart=None):
        cart = self.get_object(pk)
        meal_obj = Meal.objects.get(id=request.data["meal"])
        cart.meal.remove(meal_obj)
        cart.save()
        serializer = CartSerializer(cart)
        return Response(serializer.data)




class CartModifier(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

##### Orders

#### create a new Order
class OrderAdd(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


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




#### ### search for Order by Client ID
class OrderClientSearch(APIView):
    def get_object(self, client):
        try:
            return Order.objects.filter(client=client)
        except Order.DoesNotExist:
            raise Http404

    def get(self, request, client, format=None):
        order = self.get_object(client)
        serializer = OrderSerializer(order, many=True)
        return Response(serializer.data)