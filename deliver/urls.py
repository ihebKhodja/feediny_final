from django.urls import path
from . import views

app_name = 'deliver'

urlpatterns = [
    path('restaurant/', views.RestaurantList.as_view(), name='c_restaurant'),  # create restaurant
    path('restaurant/<int:pk>', views.RestaurantDetail.as_view(), name='r_u_d_restaurant'),# retrieve update delete restaurant
    path('meal/', views.MealCreate.as_view(), name='create_meal'),
    path('meal/list/<int:pk>', views.MealList.as_view(), name='listByIdMeal'),
    path('meal/<int:restaurant>', views.MealSearch.as_view(), name='ByRestaurantId_meal'),
    path('cart/', views.CartList.as_view(), name='CartList'),
    path('cart/add/', views.CartAdd.as_view(), name='AddtoCart'),
    # path('manager/', views.ManagerList.as_view(), name='user_list'),
    # path('manager/sign_up/', views.ManagerDetail.as_view(), name='user_detail'),
    # path('client/registration/',views.ClientCreate.as_view(), name='create_client')

]