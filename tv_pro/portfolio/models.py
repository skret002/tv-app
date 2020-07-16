from django.db import models
from tinymce.models import HTMLField


class Portfolio(models.Model):
    title = models.CharField(max_length=100, blank=True, null=False, verbose_name="Заголовок")
    prew_img = models.ImageField(upload_to='./portfolio/', verbose_name="Основное фото")
    content = HTMLField(max_length=1000, blank=True, null=True, verbose_name="Текст-Статья")
    def __str__(self):
        return "%s  %s  %s " % (self.title, self.prew_img, self.content)

    class Meta:
        db_table = 'Portfolio'
        managed = True
        verbose_name = 'Фото и контент'
        verbose_name_plural = 'Фото и контент'

class PortfolioImg(models.Model):
    img = models.ImageField(upload_to='./portfolio/', null=False, verbose_name="Дополнительное фото")
    portfolio = models.ForeignKey(Portfolio, related_name='Stor', on_delete=models.CASCADE)

    def __str__(self):
        return "%s %s " % (self.portfolio, self.img)

    class Meta:
        db_table = 'portfolio_img'
        managed = True
        verbose_name = 'Дополнительные фото'
        verbose_name_plural = 'Дополнительные фото'

