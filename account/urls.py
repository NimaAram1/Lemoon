from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenRefreshView

app_name = "account"


urlpatterns = [
   path("wtype/registeration", views.RegisterationApiView.as_view(), name="registeration"),
   path("wtype/login", views.LoginApiView.as_view(), name="login"),
   path("wtype/login-refresh", TokenRefreshView.as_view() ,name="loginRefresh"),
   path("wtype/logout", views.LogoutApiView.as_view(), name="logout"),
   path("wtype/verify-code-enter/secret/<str:email>", views.VerifyCodeEnter.as_view(), name="verify")
]
