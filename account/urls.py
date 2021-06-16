from django.urls import path
from . import views
from .views import *

app_name='account'

urlpatterns=[
    path('manager/', views.ManagerList.as_view(),   name='managers_list'),
    # path('user/', views.UserList.as_view(), name='user_list'),
    path('manager/<int:pk>/', views.ManagerDetail.as_view(),name='manager_byId'),
    path('manager/register/', RegisterManager,name='manager_registration'),
    path('manager/signin/', LoginUser, name='manager_login'),
    path('client/', views.ClientList.as_view(),name='clients_list'),
    path('client/<int:pk>/', views.ClientDetail.as_view(),name='Client_byId'),
    path('client/register/', RegisterClient, name='manager_login'),
    path('client/signin/', LoginUser, name='manager_login'),



]