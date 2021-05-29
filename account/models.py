'''
    Lemoon Database Design 
    @Account Part
    Tables
          -> User
'''
from rest_framework_simplejwt.tokens import RefreshToken
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .managers import UserManager
import datetime
from django.db.models import Q


class User(AbstractBaseUser):

    '''
        User Table
        Authentication with email 
    '''

    email = models.EmailField(max_length=120,verbose_name='ایمیل',help_text='ایمیلتونو به شکل صحیح وارد کنید',unique=True)
    first_name = models.CharField(max_length=100,verbose_name='نام',help_text='در اینجا نام خود را وارد کنید')
    last_name = models.CharField(max_length=100,verbose_name='نام خانوادگی',help_text='در اینجا نام خانوادگی خود را وارد کنید')
    birth_date = models.DateField(verbose_name='تاریخ تولد')
    is_active = models.BooleanField(default=True) 
    is_admin = models.BooleanField(default=False) 
    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['birth_date','first_name','last_name']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True   

    @property
    def is_staff(self):
        return self.is_admin 

    class Meta:
        verbose_name = 'اکانت'
        verbose_name_plural = 'اکانت ها'
        indexes = [
            models.Index(name="email_user_idx",fields=['email'])
        ]
        constraints = [
            models.CheckConstraint(name="check_birth_date",check=models.Q(birth_date__lte=f"{datetime.date.today().year-10}-01-01")) 
        ]             


# pull requests in this file may not acceptable