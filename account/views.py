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

@api_view(['POST',])



# class RegisterManager(APIView):
#     serializer_class = RegistrationManagerSerializer
#
#     def post(self, request, *args, **kwargs):
#         serializer = RegistrationManagerSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         manager = serializer.save()
#
#         return Response({
#             "manager": RegistrationManagerSerializer(manager, context=self.get_serializer_context()).data,
#             "token": AuthToken.objects.create(manager)[1]
#         })
