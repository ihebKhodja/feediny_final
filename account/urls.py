from django.urls import path
from . import views
from .views import LoginManager, RegisterManager

app_name='account'

urlpatterns=[
    path('manager/', views.ManagerList.as_view(),name='managers_list'),
    path('manager/<int:pk>/', views.ManagerDetail.as_view(),name='manager_detail'),
    path('manager/register/', RegisterManager,name='manager_registration'),
    path('manager/signin/', LoginManager, name='manager_login'),


]