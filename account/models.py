from django.contrib.auth.models import PermissionsMixin, User
from deliver.models import *


class Manager(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=12, null=True)
    USERNAME_FIELD = 'phone_number'
    is_superuser = False
    is_staff = False

    def __str__(self):
        return str(self.phone_number)


class Client(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=12, null=True)
    delivery_location = models.CharField(max_length=512, blank=True)
    lat = models.FloatField(null=True, blank=True)
    lng = models.FloatField(null=True, blank=True)
    USERNAME_FIELD = 'phone_number'
    is_superuser = False
    is_staff = False


    def __str__(self):
        return str(self.phone_number)








