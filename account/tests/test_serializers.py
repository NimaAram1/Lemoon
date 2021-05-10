from django.test import TestCase
from django.contrib.auth import get_user_model
from ..serializers import RegisterationJwtSerializer

class JwtCreateUserTests(TestCase):

    def test_create_user(self):
        
        User = get_user_model()
        user = User.objects.create_user(email="majid@email.com",first_name="majid",
        last_name="majidi",birth_date="2000-05-22",password="mybestpassword")
        user_serializer = RegisterationJwtSerializer(data=user)

        # testing parts

        self.assertEqual(user_serializer.initial_data.password,user.password)
        self.assertEqual(user_serializer.initial_data.email,user.email)
        self.assertEqual(user_serializer.initial_data.first_name,user.first_name)
        self.assertEqual(user_serializer.initial_data.last_name,user.last_name)
        self.assertEqual(user_serializer.initial_data.birth_date,user.birth_date)
        self.assertNotEqual(user_serializer.initial_data.password,"mybestpassword")   