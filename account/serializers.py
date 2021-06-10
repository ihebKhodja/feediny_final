from rest_framework import serializers
from rest_framework.authtoken.models import Token

from deliver.models import *
from .models import *


class ManagerSerializer(serializers.ModelSerializer):
    # restaurant = serializers.PrimaryKeyRelatedField(many=True, queryset=Meal.objects.all())

    class Meta:
        model = Manager
        fields = ['id', 'phone_number']

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id','phone_number','delivery_location','lat','lng']
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


# class ClientSerializer(serializers.ModelSerializer):
# client= Client(user=user, email= email, username= username)
# class Meta:
#     model = Client
#     fileds = ['user.email', 'user.username','user.password']
#     extra_kwargs = {
#         'password': {'write_only': True}
#     },
#
#     def save(self):
#         client = Client(
#             email=self.validated_data['user.email'],
#             username=self.validated_data['user.username'],
#         )
#         password=self.validated_data['user.password']
#         client.set_password(password)
#         client.save()
#         return client
# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('username', 'first_name', 'last_name', 'email')

class AddManagerSerializer(serializers.ModelSerializer):
    password = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = Client
        fields = ['id','phone_number','delivery_location','lat','lng','password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = User.objects.create(username=self.validated_data['phone_number'])
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password != password2:
            raise serializers.ValidationError({'password': 'Passwords must match'})
        user.set_password(password)
        user.save()
        #token = Token.objects.create(user=user)
        manager = Manager.objects.create(user=user, phone_number=validated_data['phone_number'])#,token=token

        manager.save()
        return user, manager




class AddClientSerializer(serializers.ModelSerializer):
        password = serializers.CharField(style={'input_type': 'password'}, write_only=True)
        password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

        class Meta:
            model = Client
            fields = ['id', 'phone_number','delivery_location','lat','lng','password', 'password2']
            extra_kwargs = {
                'password': {'write_only': True}
            }

        def create(self, validated_data):
            user = User.objects.create(username=self.validated_data['phone_number'])
            password = self.validated_data['password']
            password2 = self.validated_data['password2']
            if password != password2:
                raise serializers.ValidationError({'password': 'Passwords must match'})
            user.set_password(self.validated_data['password'])
            user.save()

            manager = Manager.objects.create(user=user, phone_number=validated_data['phone_number'],
                                             delivery_location=self.validated_data['delivery_location'],
                                             lat= self.validated_data['lat'],lng=self.validated_data['lng'])

            manager.save()
            return user, manager

    # def create(self, validated_data):
    #     user = UserSerializer.create(UserSerializer(), validated_data=user_data)
    #     manager = Manager.objects.update_or_create(user=user,subject_major=validated_data.pop('subject_major'))
    #     manager.save()
    #     return manager
