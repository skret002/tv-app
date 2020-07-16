from django.db import models
from tinymce.models import HTMLField
from tv_backend.models import PagesAboutOfMalfunctions
# Create your models here.
MALFUNK = [((str(i.id), i.title)) for i in PagesAboutOfMalfunctions.objects.all()]

class TypeLcd(models.Model):
    type_lcd = models.CharField(max_length=150, blank=True, null=False, verbose_name="Тип аппарата (монитор, жк, плазма)")
    type_lcd_img = models.ImageField(upload_to='./type_lcd_img/', verbose_name="Тип апарата наглядно+")

    def __str__(self):
        return "%s %s " % (self.type_lcd, self.type_lcd_img)


    class Meta:
        verbose_name = 'Тип аппарата'
        verbose_name_plural = 'Тип аппарата'



class LogoTv(models.Model):
    flag = models.CharField(max_length=25, blank=True, null=False, verbose_name="подпись логотипа")
    logo_brend = models.ImageField(upload_to='./logo_brend/', verbose_name="логотип бренда")

    def __str__(self):
         return "%s %s  " % (self.flag, self.logo_brend)

    class Meta:
        verbose_name = 'Логотип бренда'
        verbose_name_plural = 'Логотипы брендов'

class NameBrend(models.Model):
    brend_name = models.CharField(max_length=75, blank=True, null=False)
    logo = models.ForeignKey(LogoTv, on_delete=models.CASCADE, verbose_name="Выбрать логотип")
    def __str__(self):
         return "%s %s" % (self.brend_name, self.logo)

    class Meta:
        verbose_name = 'Имя брендов'
        verbose_name_plural = 'Имена брендов'



class TvBrend(models.Model):
    brend_name = models.ForeignKey(NameBrend, on_delete=models.CASCADE, verbose_name="Имя бренда")
    type_lcd = models.ManyToManyField(TypeLcd, verbose_name="тип аппарата")
#    size_tv = models.ForeignKey(Malfunks, on_delete=models.CASCADE,
#                                verbose_name="Диаганаль аппарата, неисправвность и цена")

    def __str__(self):
        return "%s   %s" % (self.brend_name, self.type_lcd)

    class Meta:
        verbose_name = 'Бренд телевизора'
        verbose_name_plural = 'Бренды телевизоров'

class Price(models.Model):
    brend_size = models.ForeignKey(TvBrend, on_delete=models.CASCADE, verbose_name="выбрать аппарат")
    def __str__(self):
        return "%s " % (self.brend_size)

    class Meta:
        verbose_name = 'Аппарат, неисправность и цена'
        verbose_name_plural = 'Аппараты, неисправности и цены'


class Malfunks(models.Model):
    malfunk = models.CharField(max_length=100, choices=MALFUNK, verbose_name="Тип неисправности")
    price = models.ForeignKey(Price, on_delete=models.CASCADE, verbose_name="Девайс и его параметры")
    def __str__(self):
        return "%s %s  " % (self.malfunk, self.price)

    class Meta:
        verbose_name = 'Тип неисправности'
        verbose_name_plural = 'Типы неисправностей'


class TvSizePrice(models.Model):
    size = models.CharField(max_length=150, blank=True, null=False, verbose_name="Диаганаль телевизора")
    price = models.CharField(max_length=50, blank=True, null=False)
    malfunk = models.ForeignKey(Malfunks, on_delete=models.CASCADE, verbose_name="malfunk")

    def __str__(self):
        return "%s %s %s  " % (self.size, self.price, self.malfunk)

    class Meta:
        verbose_name = 'Диаганаль телевизора'
        verbose_name_plural = 'Диаганали телевизоров'
