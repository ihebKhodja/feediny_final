from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.authtoken.models import Token

from deliver.models import *
from .models import *


# class ManagerSerializer(serializers.ModelSerializer):
#     restaurant = serializers.PrimaryKeyRelatedField(many=True, queryset=Meal.objects.all())
#     class Meta:
#         model = Manager
#         fields = ['id', 'user', 'restaurant']
#
#
#
# class ManagerSerializer(serializers.ModelSerializer):
#     """A serializer for our user profile objects."""
#
#     class Meta:
#         model = models.Manager
#         fields = ('id', 'email', 'name', 'password')
#         extra_kwargs = {'password': {'write_only': True}}
#
#     def create(self, validated_data):
#
#         user = models.Manager(
#             email=validated_data['email'],
#             name=validated_data['name']
#         )
#
#         user.set_password(validated_data['password'])
#         user.save()
#
#         return user



class RegistrationManagerSerializer(serializers.ModelSerializer):

    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = Manager
        fields = ['id','first_name','last_name','username','email','password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self,validated_data):
        user = User.objects.create(
            username=self.validated_data['username'],
            first_name=self.validated_data['first_name'],
            last_name=self.validated_data['last_name'])

        user.set_password(self.validated_data['password'])
        user.save()
        token = Token.objects.create(user= user)
        manager = Manager.objects.create(user=user, user_name=validated_data['username'],
                                first_name=self.validated_data['first_name'],
                                last_name=self.validated_data['last_name'], token= token)

        manager.save()
        return user, manager
