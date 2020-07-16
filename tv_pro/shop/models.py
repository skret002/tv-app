from django.db import models
from tinymce.models import HTMLField

ORDER_STATUS = [
    ('0', 'Ждет обработки'),
    ('1', 'Отправлен в ригион'),
    ('2', 'Выдан курьеру'),
    ('3', 'Завершен')
]

DELIVERY_STATUS = [
    ('0', 'Доставка по СПБ'),
    ('1', 'Отправить в регион'),
    ('2', 'Самовывоз')
]

STOCK = [
    ('0', 'В наличии'),
    ('1', 'Товара нет в наличии'),
    ('2', 'Скоро появится в продаже')
]
STATUS_PARTS=[
    ('0', 'БУ'),
    ('1', 'НОВЫЙ'),
   ( '2', 'Под восстановление')
]
GUARANT=[
    ('1 день на проверку', '1 день на проверку'),
    ('нет',  'нет'),
    ('3 дня',  '3 дня'),
    ('14 дней',  '14 дней'),
    ('30 дней', '30 дней')
]
class Category(models.Model):
    title = models.CharField(max_length=100, blank=True, null=False, verbose_name="Название категории")
    def __str__(self):
        return "%s  " % (self.title)

    class Meta:
        db_table = 'CategoryShop'
        managed = True
        verbose_name = 'Категория запчасти'
        verbose_name_plural = 'Категории для запчастей'


class OrderShop(models.Model):
    order_status = models.CharField(max_length=1, default=0, choices=ORDER_STATUS,
                                    null=False, verbose_name="Статус Заказа")
    delivery_status = models.CharField(max_length=1, default=0, choices=DELIVERY_STATUS,
                                       null=False, verbose_name="Тип доставки")
    name = models.CharField(max_length=100, blank=True, null=False, verbose_name="Имя")
    phone = models.CharField(max_length=100, blank=True, null=False, verbose_name="Телефон")
    address = models.CharField(max_length=150, blank=True, null=True, verbose_name="адрес")
    total_price = models.IntegerField(verbose_name="Общая сумма заказа")

    def __str__(self):
        return "%s  %s %s  %s %s %s " % (self.order_status, self.delivery_status, self.name, self.phone, self.address, self.total_price)

    class Meta:
        db_table = 'OrderShop'
        managed = True
        verbose_name = 'Заказ с Магазина'
        verbose_name_plural = 'Заказы с магазина'

class Parts(models.Model):
    title = models.CharField(max_length=100, blank=True, null=False, verbose_name="Название запчасти")
    price = models.IntegerField(blank=True, null=False, verbose_name="Цена запчасти")
    stock = models.CharField(max_length=1, choices=STOCK, null=False,
                             default=1, verbose_name="В наличии?")
    delivery_of_spb = models.IntegerField(default=500, blank=True, null=False, verbose_name="Цена доставки по СПБ")
    delivery_of_region = models.BooleanField(default=True,blank=True, null=False, verbose_name="можем ли отправить в регион")
    status_part = models.CharField(max_length=1, choices=STATUS_PARTS, null=False, verbose_name="Состояние товара")
    guarantee = models.CharField(max_length=25, choices=GUARANT, null=False,
                                 default='1 день на проверку', verbose_name="Гарантия")
    f_img = models.CharField(max_length=300, null=True, verbose_name="Основное фото")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    order = models.ForeignKey(OrderShop, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return "%s %s %s %s %s %s %s %s " % (self.title, self.price, self.category, self.stock, self.delivery_of_region, self.delivery_of_spb,
                                                                            self.status_part, self.guarantee)
    class Meta:
        db_table = 'Parts'
        managed = True
        verbose_name = 'Запчасть'
        verbose_name_plural = 'Запчасти'


class ProductInOrder(models.Model):
    order = models.ForeignKey(OrderShop,on_delete=models.CASCADE,  blank=True, null=True, default=None)
    product = models.ForeignKey(Parts, on_delete=models.CASCADE, blank=True, null=True, default=None,verbose_name="Товар")
    count = models.IntegerField(default=1, verbose_name="Кол-во в заказе")
    is_active = models.BooleanField(default=True, verbose_name="Подтвержден")
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s" % self.product.title

    class Meta:
        verbose_name = 'Товар в заказе'
        verbose_name_plural = 'Товары в заказе'

class PartsImg(models.Model):
    img = models.ImageField(upload_to='./parts_img/', null=False, verbose_name="Фото запчасти")
    parts = models.ForeignKey(Parts, on_delete=models.CASCADE)

    def __str__(self):
        return "%s  %s  " % (self.img, self.parts)

    class Meta:
        db_table = 'PartsImg'
        managed = True
        verbose_name = 'Фото'
        verbose_name_plural = 'Фотографии'


