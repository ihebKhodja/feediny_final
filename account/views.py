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


##Register API

@api_view(['POST', ])
def RegisterManager(request):
    serializer = RegistrationManagerSerializer(data=request.data)
    data= {}
    if serializer.is_valid():
        manager = serializer.save()
        data['response'] = 'successfully registered new user.'
        data['phone_number'] = manager.phone_number
        #return Response(data=data, status=status.HTTP_201_CREATED)
    else:
        #return Response(serializer.errors)
        data = serializer.errors
    return Response(data)

@api_view(['POST', ])
def LoginManager(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request,username=username, password=password)
    token, created = Token.objects.get_or_create(user=user)
    if user is not None:
        login(request,user)
        return Response({'token':token.key, 'id':user.pk}, status=status.HTTP_200_OK)
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
