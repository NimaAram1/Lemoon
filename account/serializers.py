from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken, TokenError



User = get_user_model()

class RegisterationJwtSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True,required=True,help_text='یک رمز عبور امن وارد نمایید')
    repeated_password = serializers.CharField(write_only=True,required=True,help_text="یک رمز عبور امن وارد نمایید")
    class Meta:
        model = User
        fields = ["email", "first_name", "last_name", "birth_date", "password","repeated_password"]

    def validate(self, data):
        if data['password'] and data["repeated_password"] and data['password'] != data["repeated_password"]:
            raise serializers.ValidationError("رمز عبورو تایید آن باید یکی باشد")
        return data

    def create(self, validated_data):
        validated_data["password"] = make_password(validated_data.get("password"))
        return super(RegisterationJwtSerializer, self).create(validated_data)      


class LoginJwtSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(write_only=True, max_length=220, min_length=6, help_text="ایمیل خود را وارد نمایید")
    password = serializers.CharField(write_only=True, required=True, help_text='رمز عبور خود را وارد نمایید') 
    class Meta:
        model = User
        fields = ["email","password"]

    def validate(self, data):
        email = data["email"]
        password = data["password"]
        user = authenticate(email=email, password=password)

        if not user:
            raise AuthenticationFailed("رمز عبور یا ایمیل شما صحیح نمی باشد.")

        elif not user.is_active:
            raise AuthenticationFailed("اکانت شما بن شده است؛ لطفا با مدیر سایت هماهنگ کنید")

        return super().validate(data)


class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    default_error_messages = {
        "پیام": "توکن شما نامعتبر است"
    } 

    def validate(self, data):
        self.token = data["refresh"]

        return data

    def save(self, **kwargs):

        try:
            RefreshToken(self.token).blacklist()
        except TokenError:
            self.fail("توکن شما نامعتبر است")       