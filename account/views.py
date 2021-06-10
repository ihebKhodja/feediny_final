from django.contrib.auth import authenticate, login
from django.db.migrations import serializer
from knox.models import AuthToken
from rest_framework.decorators import api_view
from rest_framework.templatetags.rest_framework import data
from rest_framework.views import APIView
from .models import *
from .serializers import *
from django.contrib.auth.models import User
from rest_framework import generics, status
from rest_framework import generics, permissions
from rest_framework.response import Response

from .serializers import *


class ManagerList(generics.ListAPIView):
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer


class ManagerDetail(generics.RetrieveAPIView):
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer

class ClientList(generics.ListAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class ClientDetail(generics.RetrieveAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

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

# class RegisterManager(generics.GenericAPIView):
#     serializer_class = RegistrationManagerSerializer
#
#     def post(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
# 			manager = serializer.save()
#
# 			return Response({
# 				"manager": RegistrationManagerSerializer(manager, context=self.get_serializer_context()).data,
# 				"token": AuthToken.objects.create(manager)[1]})
#
# 		else:
# 			return Response(serializer.errors)
