from django.test import TestCase
from .models import Resturant, Foods, Comments, Order 
from django.utils.text import slugify
from django.contrib.auth import get_user_model
class ResturantModelTests(TestCase):

    def test_create_resturant(self):
        resturant = Resturant.objects.create(name="رستوران مجید",slug=slugify("رستوران مجید",allow_unicode=True),
        cover="media/uploads/images/resturants/test.jpg",descriptions="غذا خوشمزه")
        self.assertEqual(resturant.name,"رستوران مجید")
        self.assertEqual(resturant.slug,'رستوران-مجید')
        self.assertEqual(resturant.cover,'media/uploads/images/resturants/test.jpg')
        self.assertEqual(resturant.descriptions,"غذا خوشمزه")

class FoodsModelTests(TestCase):

    def setUp(self):
        User = get_user_model()
        user = User.objects.create_user(email="maji@email.com",first_name="majid",last_name="majidi",birth_date='2000-08-25',password="sdF!f1245")
        self.resturant = Resturant.objects.create(name="رستوران مجیدی",slug=slugify("رستوران مجیدی",allow_unicode=True),
        cover="media/uploads/images/resturants/testi.jpg",descriptions="غذا خوشمزهی")
        self.comment = Comments.objects.create(user=user,body="بد مزه بود")
        self.food = Foods(title="خورش",description="خورش خوشمزه",
        cover="media/uploads/images/foods/test.jpg",foods_resturant=self.resturant,price=50,
        pointByCheif=5.6)
        self.food.save()
        self.food.comments.add(self.comment)

    def test_create_foods(self):
        self.assertEqual(self.food.title,'خورش')
        self.assertEqual(self.food.description,"خورش خوشمزه") 
        self.assertEqual(self.food.cover,"media/uploads/images/foods/test.jpg")  
        self.assertTrue(Foods.objects.filter(comments=self.comment))
        self.assertTrue(Foods.objects.filter(foods_resturant=self.resturant)) 
        self.assertEqual(self.food.price,50)   
        self.assertEqual(self.food.pointByCheif,5.6)                 

class UtilsTests(TestCase):

    def test_create_order(self):
        User = get_user_model()
        user = User.objects.create_user(email="maji2@email.com",first_name="majid",last_name="majidi",birth_date='2000-08-25',password="sdF!f1245")
        resturant = Resturant.objects.create(name="رستوران مجیدیی",slug=slugify("رستوران مجیدیی",allow_unicode=True),
        cover="media/uploads/images/resturants/testis.jpg",descriptions="غذا خوشمزهی")
        food = Foods.objects.create(title="خورشی",description="خورش خوشمزه",cover="media/uploads/images/foods/test.jpg",
        foods_resturant=resturant,price=50,pointByCheif=5.6)
        order = Order.objects.create(name="سفارش شماره 2",timeDelay=30,user=user)
        order.foods.add(food)
        
        # test part

        self.assertEqual(order.name,"سفارش شماره 2") 
        self.assertEqual(order.timeDelay,30)
        self.assertEqual(order.user,user)
        self.assertTrue(Order.objects.filter(foods=food))


    def test_create_comment(self):
        User = get_user_model()
        user = User.objects.create_user(email="maji2@email.com",first_name="majid",last_name="majidi",birth_date='2000-08-25',password="sdF!f1245")
        comment = Comments.objects.create(user=user,body="غذای خوبی بود")

        # test part

        self.assertEqual(comment.user,user)
        self.assertEqual(comment.body,"غذای خوبی بود")
