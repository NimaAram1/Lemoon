from django.shortcuts import render
from django.views import generic
from rest_framework import status
from rest_framework import generics
from rest_framework.views import APIView, Response
from .serializers import (
    RegisterationJwtSerializer, 
    LoginJwtSerializer, 
    LogoutSerializer
)
from django.contrib.auth import get_user_model
from rest_framework.generics import GenericAPIView
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from django.utils.decorators import method_decorator
from .utils import generate6Code
from django.core.mail import send_mail

User = get_user_model()


class RegisterationApiView(APIView):

    '''
    registeration view
    via jwt
    ''' 
    def post(self,request):
        data = RegisterationJwtSerializer(data=request.data) 
        if data.is_valid():
            User.objects.create_user(email=data.validated_data["email"],
            first_name=data.validated_data["first_name"],last_name=data.validated_data["last_name"],
            password=data.validated_data["password"],birth_date=data.validated_data["birth_date"])
            user = authenticate(email=data.validated_data["email"], password=data.validated_data["password"])
            tokens = RefreshToken.for_user(user) 
            return Response({
                "message":"اکانت شما با موفقیت ساخته شد",
                "access": str(tokens.access_token),
                "refresh": str(tokens)
                }
            , status=status.HTTP_200_OK)
        else:
            return Response(data.errors)
           

class LoginApiView(GenericAPIView):

    '''
    login view 
    via jwt
    '''
    serializer_class = LoginJwtSerializer
    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data["email"]
        password = serializer.validated_data["password"]
        user = authenticate(email=email, password=password)
        tokens = RefreshToken.for_user(user)
        return Response({
            "access": str(tokens.access_token),
            "refresh": str(tokens)
        }, status=status.HTTP_200_OK)

class LogoutApiView(generics.GenericAPIView):

    serializer_class = LogoutSerializer
    permission_classes = (IsAuthenticated, )

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({
            "پیام": "شما با موفقیت خارج شدید"
        }, status=status.HTTP_204_NO_CONTENT)

