from django.db import models
from tinymce.models import HTMLField
# Create your models here.


class SlideInHome(models.Model):
    slaid_title = models.CharField(max_length=50, blank=True, null=False)
    content = HTMLField(max_length=500, blank=True, null=False)
    image = models.ImageField(upload_to='./slider/')

    def __str__(self):
        return "%s   %s" % (self.slaid_title, self.content)

    class Meta:
        verbose_name = 'Текст в слайд на главную'
        verbose_name_plural = 'Тексты в слайд на главную'


class Home(models.Model):
    phone = models.CharField(blank=True, null=False, max_length=12)
    adress = models.CharField(max_length=50, blank=True, null=False)
    email = models.EmailField(max_length=254, blank=True, null=False)
    time_work = models.CharField(max_length=50, blank=True, null=False)
    slider = models.ManyToManyField(SlideInHome, related_name="slide",)

    def __str__(self):
        return "%s  %s  %s   %s" % (self.phone, self.adress, self.email,  self.time_work)

    class Meta:
        verbose_name = 'Основные данные: тел, график и т.д'
        verbose_name_plural = 'Основные данные: тел, график и т.д'


class PagesAboutOfMalfunctions(models.Model):
    title = models.CharField(max_length=50, verbose_name="Оглавление", null=False)
    content = HTMLField(max_length=50000, blank=True, null=False, verbose_name="Текст статьи")
    def __str__(self):
        return "%s  %s " % (self.title, self.content)

    class Meta:
        verbose_name = 'Статья о неисправности'
        verbose_name_plural = 'Статьи о неисправностях'




class TypesOfMalfunctions(models.Model):
    icon = models.ImageField(upload_to='./TypesOfMalfunctions_icon/', verbose_name="Иконка  в левом углу")
    title = models.CharField(max_length=50, verbose_name="Оглавление", null=False)
    content = HTMLField(max_length=500, blank=True, null=False, verbose_name="Контент")
    link = models.ForeignKey(PagesAboutOfMalfunctions, on_delete=models.CASCADE)

    def __str__(self):
        return "%s  %s  %s " % (self.title, self.content,  self.link)

    class Meta:
        verbose_name = 'Возможные неисправности > "после слайда"'
        verbose_name_plural = 'Возможные неисправности > "после слайда"'

class AboutInHome(models.Model):
    title = models.CharField(max_length=50, verbose_name="Оглавление", null=False)
    content = HTMLField(max_length=5000, blank=True, null=False, verbose_name="Контент")
    image = models.ImageField(upload_to='./home/', verbose_name="Картинка с право")

    def __str__(self):
        return "%s  %s  %s " % (self.title, self.content,  self.image)

    class Meta:
        verbose_name = 'Блок о нас на главной'
        verbose_name_plural = 'Блок о нас на главной'

class InfoAboutOrder(models.Model):
    title = models.CharField(max_length=100, verbose_name="Оглавление", null=False)
    sub_title = models.CharField(max_length=200, verbose_name="Доп оглавление", null=False)
    video = models.FileField(verbose_name="Видео", upload_to='./home/')

    def __str__(self):
        return "%s  %s  %s " % (self.title, self.sub_title,  self.video)

    class Meta:
        verbose_name = 'Блок о заказе на главной'
        verbose_name_plural = 'Блок о заказе на главной'


class Reviews(models.Model):
    show_flag = models.BooleanField(default=True, verbose_name="Показывать отзыв на сайте?")
    name_user = models.CharField(max_length=50, verbose_name="Имя клиента", null=False)
    user_photo_link = models.URLField(verbose_name="Фото профиля")
    review = models.TextField(max_length=1000, verbose_name="Отзыв клиента")
    review_rate = models.DecimalField(max_digits=5, decimal_places=0, verbose_name="кол-во звезд")


    def __str__(self):
        return "%s  %s  %s  %s  %s  " % (self.show_flag, self.name_user,  self.user_photo_link, self.review, self.review_rate)

    class Meta:
        verbose_name = 'Отзыв на Яндекс'
        verbose_name_plural = 'Отзывы на Яндекс'
