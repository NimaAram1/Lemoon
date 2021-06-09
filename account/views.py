from django.shortcuts import render
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
from django.core.mail import send_mail
from .utils import generate6Code

User = get_user_model()


class RegisterationApiView(APIView):

    '''
    registeration view
    via jwt
    ''' 
    def post(self,request):
        data = RegisterationJwtSerializer(data=request.data) 
        if data.is_valid():
            code = generate6Code()
            user_object = User.objects.create_user(email=data.validated_data["email"],
            first_name=data.validated_data["first_name"],last_name=data.validated_data["last_name"],
            password=data.validated_data["password"],birth_date=data.validated_data["birth_date"])
            User.objects.filter(email=data.validated_data["email"]).update(verify_code=code)
            User.objects.filter(email=data.validated_data["email"]).update(is_active=False)
            send_mail("Verification Code", f"Your code is: {code}", "aramnima50@gmail.com", [f"{data.validated_data['email']}"])
            return Response({
                "message":"اکانت شما با موفقیت ساخته شد برای استفاده با کد فعالسازی آنرا فعال کنید",
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

class VerifyCodeEnter(APIView):
    
    def post(self, request, email):
        
        user_key = User.objects.filter(email=email)
        if user_key.values_list("is_active")[0][0] == True:
            return Response({"message": "this account has activated already"})
        if request.data["verify_code"] == user_key.values_list("verify_code")[0][0]:
            user_key.update(is_active=True)
            user_key.update(verify_code=None)
            try:
                user = authenticate(email=user_key.values_list("email")[0][0], password=request.data["password"])
                tokens = RefreshToken.for_user(user)
            except:
                return Response({"error": "wrong password!"})
            return Response({
                "access": str(tokens.access_token),
                "refresh": str(tokens)
            }
            )
        elif request.data["verify_code"] != user_key.verify_code:
            return Response({
                "error": "wrong code!"
            })
           

 