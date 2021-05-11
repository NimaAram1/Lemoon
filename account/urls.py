from django.urls import path, include
from . import views

app_name = "account"


urlpatterns = [
   path("wtype/registeration",views.registerationApi.as_view(),name="registeration"),
   path("wtype/login",views.loginApi.as_view(),name="login")
]
