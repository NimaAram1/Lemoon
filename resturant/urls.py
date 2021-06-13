from django.urls import path
from . import views

app_name = "resturant"


urlpatterns = [
   path("order/<int:food>", views.OrderFoodApiView.as_view(), name="orderFood")
]
