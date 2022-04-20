from logging import raiseExceptions
from django.shortcuts import render
from rest_framework import generics,status
from rest_framework.response import Response

from .models import Account
from . serializers import UserRegister,ChangePasswordSerializer

from rest_framework.permissions import IsAuthenticated
from .permissions import IsObjectOwner



# Create your views here.
class UserRegisterView(generics.ListCreateAPIView):
    serializer_class=UserRegister

    def get(self,request):
        users=Account.objects.all()
        serializer=UserRegister(users,many=True)
        return Response(serializer.data)

    def post(self,request,*args,**kwargs):
        serializer=self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user=serializer.save()
        return Response({"user":UserRegister(user,context=self.get_serializer_context()).data,
        "message":"Registered user successfully"},status=status.HTTP_201_CREATED)


class ChangePasswordView(generics.UpdateAPIView,Exception):
    queryset=Account.objects.all()
    permission_classes=[IsAuthenticated,IsObjectOwner]
    serializer_class = ChangePasswordSerializer
    def put(self,request):
        return Response({"message:Updated successfully"})