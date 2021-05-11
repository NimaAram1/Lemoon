from django.urls import path, include
from . import views
from rest_framework_simplejwt.views import TokenRefreshView

app_name = "account"


urlpatterns = [
   path("wtype/registeration",views.registerationApi.as_view(),name="registeration"),
   path("wtype/login",views.loginApi.as_view(),name="login"),
   path("wtype/login-refresh",TokenRefreshView.as_view(),name="loginRefresh")
]
