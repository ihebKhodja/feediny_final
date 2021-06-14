from rest_framework import serializers
from rest_framework.authtoken.models import Token
from deliver.models import *
from .models import *


class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manager
        fields = ['id','user', 'phone_number']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id','user', 'phone_number', 'delivery_location', 'lat', 'lng']




class AddManagerSerializer(serializers.ModelSerializer):
    password = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    first_name = serializers.CharField()
    last_name = serializers.CharField()

    class Meta:
        model = Manager
        fields = ['id', 'phone_number','first_name','last_name','password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = User.objects.create(username=self.validated_data['phone_number'],
                                   first_name=self.validated_data['first_name'],
                                   last_name=self.validated_data['last_name'])

        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        # if password != password2:
        #     raise serializers.ValidationError({'password': 'Passwords must match'})
        user.set_password(password)
        user.save()
        token = Token.objects.create(user=user)
        manager = Manager.objects.create(user=user, phone_number=validated_data['phone_number'])

        manager.save()
        return manager


class AddClientSerializer(serializers.ModelSerializer):
    password = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    first_name = serializers.CharField()
    last_name = serializers.CharField()


    class Meta:
        model = Client
        fields = ['id', 'phone_number','first_name','last_name','delivery_location', 'lat', 'lng', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = User.objects.create(username=self.validated_data['phone_number'],
                                   first_name=self.validated_data['first_name'],
                                   last_name=self.validated_data['last_name'])
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        # if password != password2:
        #     raise serializers.ValidationError({'password': 'Passwords must match'})
        user.set_password(self.validated_data['password'])
        user.save()
        token = Token.objects.create(user=user)
        client = Client.objects.create(user=user, phone_number=validated_data['phone_number'],
                                       delivery_location=self.validated_data['delivery_location'],
                                       lat=self.validated_data['lat'], lng=self.validated_data['lng'])

        client.save()
        return client

