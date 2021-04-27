from django.db import models

class Foods(models.Model):
    title = models.CharField(max_length=120,verbose_name='اسم غذا')
    description = models.TextField(verbose_name='توضیحات کامل غذا',help_text='در اینجا میتوانید توضیحات کاملی از غذا ارائه کنید')
    cover = models.ImageField(upload_to='uploads/images',verbose_name='عکس غذا',help_text='در اینجا میتوانید عکس محصول را برای جذب مشتری آپلود کنید')
    # resturant = 
    # comments =
    price = models.DecimalField(max_digits=10,decimal_places=0,verbose_name='قیمت')
    pointByCheif = models.IntegerField(verbose_name='نمره آشپز',help_text='در اینجا نمره آشپز را وارد نمایید')

    def __str__(self):
        return f'{self.title} | {self.price}'

    class Meta:
        verbose_name = 'غذا'
        verbose_name_plural = 'غذا ها'
        ordering = ['price']    
    