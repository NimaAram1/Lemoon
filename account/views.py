from django.shortcuts import render
from rest_framework.views import APIView, Response
from .serializers import RegisterationJwtSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

class registeration(APIView):

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


