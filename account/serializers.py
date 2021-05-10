from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password

User = get_user_model()

class RegisterationJwtSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True,required=True,help_text='یک رمز عبور امن وارد نمایید')
    repeated_password = serializers.CharField(write_only=True,required=True,help_text="یک رمز عبور امن وارد نمایید")
    class Meta:
        model = User
        fields = ["email", "first_name", "last_name", "birth_date", "password","repeated_password"]

    def validate_repeated_password(self):
        data = self.validated_data
        if data['password'] and data["repeated_password"] and data['password'] != data["repeated_password"]:
            raise serializers.ValidationError("رمز عبورو تایید آن باید یکی باشد")
        return data["repeated_password"]

    def create(self, validated_data):
        validated_data["password"] = make_password(validated_data.get("password"))
        return super(RegisterationJwtSerializer, self).create(validated_data)