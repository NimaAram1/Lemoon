from django.shortcuts import render
from rest_framework.views import APIView, Response
from .models import Foods, Order
from rest_framework.permissions import IsAuthenticated
from .utils import get_order_name
class OrderFoodApiView(APIView):

    permission_classes = (IsAuthenticated, )

    def post(self, request, food):
         
        if Foods.objects.filter(pk=food).exists() is False:
            return Response({
                "error": "this food isn't exist"
            })    
        count_of_food = int(request.GET.get("count", 1))
        if type(count_of_food) is type(str("")):
            return Response({
                "error": "you entered wrong value in ?count"
            })        
        food_ordered = Foods.objects.filter(pk=food).values()[0]["id"]
        name_of_order = get_order_name()
        order = Order.objects.create(name=name_of_order, timeDelay=25.00, user=request.user)
        if count_of_food == 1:
            order.foods.add(food_ordered)
        elif count_of_food > 1:
            for i in range(1, count_of_food):
                order2 = Order.objects.create(name=name_of_order, timeDelay=25.00, user=request.user)
                order2.foods.add(food_ordered) 
        return Response({
            "message": "You successfully ordered your food! check your table."
        })