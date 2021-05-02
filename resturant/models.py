'''
    Lemoon Database Design 
    @Resturant Part
    Tables
          -> Resturant
          -> Foods
          -> Order
          -> Comments
'''


from django.db import models
from django.contrib.auth import get_user_model

class Resturant(models.Model):

    '''
        Resturant Class 
        Descriptions:
            *Foods field get all of the foods from specefic resturant
            *Indexing resturant name can increase app performance 
    '''

    name = models.CharField(max_length=150,verbose_name='اسم رستوران',help_text='در اینجا اسم رستوران را وارد کنید')
    slug = models.SlugField(max_length=250,verbose_name='لینک رستوران',blank=True)
    cover = models.ImageField(upload_to='uploads/images/resturants',verbose_name='عکس رستوران',help_text='در اینجا میتوانید عکسی برای دیده شدن بهتر رستورانتان بگذارید')
    descriptions = models.TextField(verbose_name='درباره رستوران',help_text='در اینجا میتوانید درباره رستوران خود اطلاعاتی را وارد کنید')
    foods = models.ForeignKey('Foods',on_delete=models.SET_NULL,verbose_name="غذا ها")
    createdDate = models.DateTimeField(auto_now=True)
    updatedDate = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "رستوران"
        verbose_name_plural = "رستوران ها"
        ordering = ['name']
        indexes = [
            models.Index(name="name_resturant_idx",fields=['name'])
        ]     

class Foods(models.Model):

    '''
        Foods Class
        No any special thing, just a simple table
    '''
    
    title = models.CharField(max_length=120,verbose_name='اسم غذا')
    description = models.TextField(verbose_name='توضیحات کامل غذا',help_text='در اینجا میتوانید توضیحات کاملی از غذا ارائه کنید')
    cover = models.ImageField(upload_to='uploads/images/foods',verbose_name='عکس غذا',help_text='در اینجا میتوانید عکس محصول را برای جذب مشتری آپلود کنید')
    resturant = models.OneToOneField(Resturant,on_delete=models.CASCADE,verbose_name="رستورانی که این غذا را پخت میکند") 
    comments = models.ManyToManyField('Comments',verbose_name='نظرات')
    price = models.DecimalField(max_digits=10,decimal_places=0,verbose_name='قیمت')
    pointByCheif = models.IntegerField(verbose_name='نمره آشپز',help_text='در اینجا نمره آشپز را وارد نمایید')
    createdDate = models.DateTimeField(auto_now=True)
    updatedDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title} | {self.price}'

    class Meta:
        verbose_name = 'غذا'
        verbose_name_plural = 'غذا ها'
        order_with_respect_to = 'resturant'

class Order(models.Model):

    '''
        Order Table
        No any special thing, just a simple table
    '''

    name = models.CharField(max_length=150,blank=True,verbose_name='عنوان سفارش')
    timeDelay = models.IntegerField(verbose_name='تایمر سفارش',blank=True)
    user = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    foods = models.ManyToManyField(Foods,verbose_name='غذا های سفارش شده')
    createdDate = models.DateTimeField(auto_now=True)
    updatedDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} | {self.user}'

    class Meta:
        verbose_name = 'سفارش'
        verbose_name_plural = 'سفارشات'
        ordering = ['-timeDelay']

class Comments(models.Model):

    '''
        Comments Table
        No any special thing, just a simple table
    '''

    user = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    body = models.TextField(verbose_name='نظر',help_text='در اینجا میتونید نظرتون رو وارد کنید')
    createdDate = models.DateTimeField(auto_now=True)
    updatedDate = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'{self.user} | {self.body[:15]}...'

    class Meta:
        verbose_name = 'نظر'
        verbose_name_plural = 'نظرات'
        ordering = ['createdDate']


# pull requests in this file may not acceptable  