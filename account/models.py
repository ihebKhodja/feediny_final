from django.contrib.auth.models import PermissionsMixin, User
from deliver.models import *


class Manager(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=12, null=True)
    USERNAME_FIELD = 'phone_number'
    is_superuser = False

    def __str__(self):
        return self.user.username


class Client(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=12, null=True)
    delivery_location = models.CharField(max_length=512, blank=True)
    lat = models.FloatField(null=True, blank=True)
    lng = models.FloatField(null=True, blank=True)
    USERNAME_FIELD = 'phone_number'
    is_superuser = False

    def __str__(self):
        return self.user.username


# class UserProfileManager(BaseUserManager):
#
#     def create_user(self, email, name, password=None):
#
#         if not email:
#             raise ValueError('Users must have an email address.')
#
#         email = self.normalize_email(email)
#         user = self.model(email=email, name=name,)
#
#         user.set_password(password)
#         user.save(using=self._db)
#
#         return user
#
#     def create_superuser(self, email, name, password):
#
#         user = self.create_user(email, name, password)
#
#         user.is_superuser = True
#         user.is_staff = True
#         user.save(using=self._db)
#
#         return user


# class Manager(AbstractBaseUser, PermissionsMixin):
#
#     email = models.EmailField(max_length=255, unique=True)
#     name = models.CharField(max_length=255)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)
#
#     objects = UserProfileManager()
#
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['name']
#
#
#     def __str__(self):
#
#         return self.email


# class Client(AbstractBaseUser, PermissionsMixin):
#
#     email = models.EmailField(max_length=255, unique=True)
#     username = models.CharField(max_length=255, unique=True)
#     name = models.CharField(max_length=255)
#     phone_number = models.CharField(max_length=10)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)
#
#     objects = UserProfileManager()
#
#     USERNAME_FIELD = 'username'
#     REQUIRED_FIELDS = ['name']
#
#
#     def __str__(self):
#
#         return self.phone_number