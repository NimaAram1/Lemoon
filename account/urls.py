from django.urls import path, include
from . import views

app_name = "account"


urlpatterns = [
   path("wtype/registeration",views.registeration.as_view(),name="registeration")
]
