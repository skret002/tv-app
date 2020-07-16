from django.db import models
from tinymce.models import HTMLField

class AdditionalStaff(models.Model):
    name = models.CharField(max_length=50, blank=True, null=False,verbose_name="Имя сотрудника")
    area = models.CharField(max_length=50, blank=True, null=False, verbose_name="Зона ответственности")
    phone_number = models.CharField(max_length=50, blank=True, null=False, verbose_name="Контактный номер")
    avatar = models.ImageField("Аватар", upload_to="./state_avatar")

    def __str__(self):
        return "%s %s  %s  %s " % (self.name, self.area, self.phone_number, self.avatar)

    class Meta:
        db_table = 'AdditionalStaff'
        managed = True
        verbose_name = 'Дополнительные сотрудник (футер)'
        verbose_name_plural = 'Дополнительные сотрудники (футер)'


class SaleInFooter(models.Model):
    name_sale = models.CharField(max_length=50, blank=True, null=False, verbose_name="Название акции")
    description_sale = models.CharField(max_length=150, blank=True, null=False, verbose_name="Короткое описание акции")
    size_sale = models.IntegerField("Размер скидки")

    def __str__(self):
        return "%s %s  %s " % (self.name_sale, self.description_sale, self.size_sale)

    class Meta:
        db_table = 'SaleInFooter'
        managed = True
        verbose_name = 'Акция в подвале'
        verbose_name_plural = 'Скидки и Акции в подвале'

class CenterInFooter(models.Model):
    logo =  models.ImageField("Логотип в футере", upload_to="./logo_footer")
    content = HTMLField(max_length=500, blank=True, null=True)
    def __str__(self):
        return "%s %s  " % (self.logo, self.content)

    class Meta:
        db_table = 'CenterInFooter'
        managed = True
        verbose_name = 'Лого и текст в центр футера'
        verbose_name_plural = 'Лого и текст в центр футера'
