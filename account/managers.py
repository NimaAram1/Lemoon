from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, birth_date, password):
        if not email:
            raise ValueError("در ساخت حساب حتما می بایستی ایمیل را وارد نمایید")
        elif not first_name:
            raise ValueError("نام خود را وارد کنید")
        elif not last_name:
            raise ValueError("نام خانوادگی خود را وارد کنید")
        elif not birth_date:
            raise ValueError("تاریخ تولد خود را وارد نمایید")

        user = self.model(email=self.normalize_email(email),first_name=first_name,
        last_name=last_name,birth_date=birth_date)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, birth_date, password):
        user = self.create_user(email=email, first_name=first_name, last_name=last_name, birth_date=birth_date, password=password) 
        user.is_admin = True
        user.save(using=self._db)
        return user   