from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='类别名称')
    code = models.CharField(max_length=100, verbose_name='类别Code')
    add_time = models.DateTimeField(auto_now_add=True, verbose_name='添加时间')

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='商品类别')
    name = models.CharField(max_length=100, verbose_name='商品名称')
    price = models.FloatField(default=0, verbose_name='商品价格')
    serial_number = models.CharField(max_length=100, verbose_name='商品编号')
    add_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='image', verbose_name='商品')
    image = models.ImageField(upload_to='product_image', verbose_name='商品图片')
    add_time = models.DateTimeField(auto_now_add=True, verbose_name='添加时间')
