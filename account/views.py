from django.contrib.auth import authenticate, login
from django.http import Http404
from rest_framework.decorators import api_view
from rest_framework.templatetags.rest_framework import data
from rest_framework.views import APIView
from .models import *
from .serializers import *
from django.contrib.auth.models import User
from rest_framework import generics, status
from rest_framework import generics
from rest_framework.response import Response
from .serializers import *


class ManagerList(generics.ListAPIView):
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer


# class UserList(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


class ManagerDetail(generics.RetrieveAPIView):
    def get_object(self, pk):
        try:
            return Manager.objects.get(user=pk)
        except Order.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        manager = self.get_object(pk)
        serializer = ManagerSerializer(manager)
        return Response(serializer.data)


class ClientList(generics.ListAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class ClientDetail(APIView):
    def get_object(self, pk):
        try:
            return Client.objects.get(user=pk)
        except Order.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        client = self.get_object(pk)
        serializer = ClientSerializer(client)
        return Response(serializer.data)


##Register API


@api_view(['POST', ])
def RegisterManager(request):
    serializer = AddManagerSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors)


@api_view(['POST', ])
def RegisterClient(request):
    serializer = AddClientSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors)


@api_view(['POST', ])
def LoginUser(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    token, created = Token.objects.get_or_create(user=user)
    if user is not None:
        login(request, user)
        return Response({'token': token.key, 'id': user.pk}, status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

