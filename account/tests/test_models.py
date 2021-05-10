from django.test import TestCase
from django.contrib.auth import get_user_model
from django.db import IntegrityError

class AccountModelTests(TestCase):

    def test_create_account(self):

        User = get_user_model()
        user = User.objects.create_user(email="majid@email.com",first_name="majid",
        last_name="majidi",birth_date="2000-05-22",password="mybestpassword")

        # testing parts 

        self.assertEqual(user.email,"majid@email.com")
        self.assertEqual(user.first_name,"majid")
        self.assertEqual(user.last_name,"majidi")
        self.assertEqual(user.birth_date,"2000-05-22")
        self.assertNotEqual(user.password,"mybestpassword")
        self.assertEqual(user.is_active,True)
        self.assertEqual(user.is_admin,False)

    def test_create_superuser(self):

        User = get_user_model()
        user = User.objects.create_superuser(email="majid2@email.com",first_name="majid",
        last_name="majidi",birth_date="2000-05-22",password="mybestpassword")

        # testing parts 

        self.assertEqual(user.email,"majid2@email.com")
        self.assertEqual(user.first_name,"majid")
        self.assertEqual(user.last_name,"majidi")
        self.assertEqual(user.birth_date,"2000-05-22")
        self.assertNotEqual(user.password,"mybestpassword")
        self.assertEqual(user.is_active,True)
        self.assertEqual(user.is_admin,True)

    def test_create_user_under_10(self):

        User = get_user_model()
        user = User.objects.test_under_age(email="majid@email.com",first_name="small_majid",
        last_name="majidi",birth_date="2011-05-22",password="mybestpassword")

        with self.assertRaises(IntegrityError):
            user.save()