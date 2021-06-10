from django.urls import path
from . import views

app_name = 'deliver'

urlpatterns = [
    path('restaurant/', views.RestaurantList.as_view(), name='c_restaurant'),  # create restaurant
    path('restaurant/<int:pk>', views.RestaurantDetail.as_view(), name='r_u_d_restaurant'),# retrieve update delete restaurant
    path('meal/', views.MealCreate.as_view(), name='create_meal'),
    path('meal/list/<int:pk>', views.MealList.as_view(), name='listByIdMeal'),
    path('meal/<int:restaurant>', views.MealSearch.as_view(), name='ByRestaurantId_meal'),
    path('cart/', views.CartList.as_view(), name='CartList'),### get list
    path('cart/add/', views.CartAdd.as_view(), name='AddtoCart'),#### post
    path('cart/<int:pk>', views.CartModifier.as_view(), name='Update_Delete_Retrieve_Cart'),#### post delete get methods


]