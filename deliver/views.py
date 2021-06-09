from django.http import Http404
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from account.models import *
from .serializers import *
from django.contrib.auth.models import User
from .permissions import IsOwnerOrReadOnly


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
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]


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
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

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

class CartMofidier(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
####
##### User
# class ManagerList(generics.ListAPIView):
#     queryset = Manager.objects.all()
#     serializer_class = ManagerSerializer
#
#
# class ManagerDetail(generics.CreateAPIView):
#     queryset = Manager.objects.all()
#     serializer_class = ManagerSerializer
#
# class ClientCreate(generics.CreateAPIView):
#     queryset = Client.objects.all()
#     serializer_class = ClientSerializer