from django.urls import path
from . import views

app_name='account'

urlpatterns=[
    path('manager/', views.ManagerList.as_view(),name='managers_list'),
    path('manager/<int:pk>/', views.ManagerDetail.as_view(),name='manager_detail'),
    path('manager/register/', views.RegisterManager,name='manager_registration'),


]