from django.urls import path
from . import views

app_name = 'deliver'

urlpatterns = [
    path('restaurant/', views.RestaurantList.as_view(), name='list_restaurant'),  # list create restaurant
    path('restaurant/add/', views.RestaurantCreate.as_view(), name='create_restaurant'),
    path('restaurant/<int:pk>', views.RestaurantDetail.as_view(), name='r_u_d_restaurant'),# retrieve update delete restaurant
    path('meal/', views.MealCreate.as_view(), name='create_meal'),
    path('meal/list/', views.MealListAll.as_view(), name='listOfMeal'),
    path('meal/list/<int:pk>', views.MealList.as_view(), name='listByIdMeal'),
    path('meal/<int:restaurant>', views.MealSearch.as_view(), name='ByRestaurantId_meal'),
    path('cart/', views.CartList.as_view(), name='CartList'),### get list
    path('cart/add/', views.CartAdd.as_view(), name='AddtoCart'),#### post create new cart
    path('cart/add/<int:pk>', views.AddMealToCart.as_view(), name='AddMealtoCart'),  #### add meal to cart
    path('cart/delete/<int:pk>', views.deleteMealCart.as_view(), name='deleteMealfromCart'),  #### delete meal from cart
    path('cart/<int:pk>', views.CartModifier.as_view(), name='Update_Delete_Retrieve_Cart'),#### post delete get methods
    path('order/list/', views.OrderList.as_view(), name='ListOrder'),
    path('order/add/', views.OrderAdd.as_view(), name='AddtoOrder'),  #### post
    path('order/<int:restaurant>', views.OrderSearch.as_view(), name='ByRestaurantId_order'),#### orders by restaurant ID
    path('order/client/<int:client>', views.OrderClientSearch.as_view(), name='ByRestaurantId_order_client'),#### orders by client ID

]