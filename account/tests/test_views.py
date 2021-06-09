from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from ..utils import generate6Code

User = get_user_model()

class AuthenticationTests(APITestCase):
   
    def test_registeration(self):
        data = {
            "email": "majid@gmail.com",
            "first_name": "majid",
            "last_name": "majidi",
            "birth_date": "2000-01-01",
            "password": "nicepasswordihave",
            "repeated_password": "nicepasswordihave"
        }
        response = self.client.post("http://127.0.0.1:8000/api/wtype/registeration", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_login(self):
        user = User.objects.create_user(email="majid@gmail.com",first_name="majid",
        last_name="majidi",birth_date="2000-01-01",password="nicepasswordihave")
        data = {
            "email": "majid@gmail.com",
            "password": "nicepasswordihave"
        }
        response = self.client.post("http://127.0.0.1:8000/api/wtype/login", data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logout(self):
        userCreateInstance = User.objects.create_user(email="majid@gmail.com",first_name="majid",
        last_name="majidi",birth_date="2000-01-01",password="nicepasswordihave")
        user = authenticate(email="majid@gmail.com", password="nicepasswordihave")
        refreshToken = RefreshToken.for_user(user)
        data = {
            "refresh": str(refreshToken)
        }
        self.client.credentials(HTTP_AUTHORIZATION="Bearer "+str(refreshToken.access_token))
        response = self.client.post("http://127.0.0.1:8000/api/wtype/logout", data)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT) 
    
    def test_refresh_login(self):
        userCreateInstance = User.objects.create_user(email="majid@gmail.com",first_name="majid",
        last_name="majidi",birth_date="2000-01-01",password="nicepasswordihave")
        user = authenticate(email="majid@gmail.com", password="nicepasswordihave")
        refreshToken = RefreshToken.for_user(user)
        data = {
            "refresh": str(refreshToken)
        }
        response = self.client.post("http://127.0.0.1:8000/api/wtype/login-refresh", data)
        self.assertEqual(response.status_code, status.HTTP_200_OK) 

    def test_verify_code(self):
        userCreateInstance = User.objects.create_user(email="majid@gmail.com",first_name="majid",
        last_name="majidi",birth_date="2000-01-01",password="nicepasswordihave")
        code_verify = generate6Code()
        User.objects.filter(email="majid@gmail.com").update(is_active=False)
        User.objects.filter(email="majid@gmail.com").update(verify_code=code_verify)
        data = {
            "verify_code": code_verify,
            "password": "nicepasswordihave"
        }
        response = self.client.post("http://127.0.0.1:8000/api/wtype/verify-code-enter/secret/majid@gmail.com", data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)