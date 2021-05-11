from django.shortcuts import render
from rest_framework.views import APIView, Response
from .serializers import RegisterationJwtSerializer
from django.contrib.auth import get_user_model
from rest_framework.exceptions import AuthenticationFailed
import jwt, datetime

User = get_user_model()

class registerationApi(APIView):

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
            return Response({"message":"اکانت شما با موفقیت ساخته شد"})
        else:
            return Response(data.errors)


class loginApi(APIView):

    '''
    login view 
    via jwt
    '''

    def post(self,request):
        email = request.data["email"]
        password = request.data["password"]

        user = User.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed("کاربری با این مشخصات موجود نیست")

        if not user.check_password(password):
            raise AuthenticationFailed("رمز عبور شما صحیح نمی باشد")

        payload = {
            "id": user.id,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=320),
            "iat": datetime.datetime.utcnow()
        }
        try:
            token = jwt.encode(payload, 'secret', algorithm='HS256').decode("utf-8")
        except:
            token = jwt.encode(payload, 'secret', algorithm='HS256')   
        response = Response()
        response.set_cookie(key="jwt", value=token, httponly=True)
        response.data = {
            "token": token,
            "message": "با موفقیت وارد شدید"
        }
        return response
