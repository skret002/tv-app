from django.db import models
from tinymce.models import HTMLField


class AboutStaff(models.Model):
    video = models.FileField(upload_to='./video_staff', max_length=100, blank=True, null=True, verbose_name="видео на стр. о сотрудниках")

    def __str__(self):
        return "%s " % (self.video)

    class Meta:
        db_table = 'Staff_Video'
        managed = True
        verbose_name = 'Видео + Основной штат сотрудников'
        verbose_name_plural = 'Видео + Основной штат сотрудников '

class Staff(models.Model):
    name = models.CharField(max_length=50, blank=True, null=False, verbose_name="Имя сотрудника")
    avatar = models.ImageField(upload_to='./avatar_staff/', null=False, verbose_name="Фото сотрудника")
    position = models.CharField(max_length=50, blank=True, null=False, verbose_name="Должность")
    text = HTMLField(max_length=200, blank=True, null=False, verbose_name="Коротко о себе")
    video = models.ForeignKey(AboutStaff, related_name='Видео', on_delete=models.CASCADE)

    def __str__(self):
        return "%s %s %s %s  %s " % (self.name, self.avatar, self.position, self.text, self.video)

    class Meta:
        db_table = 'Staff'
        managed = True
        verbose_name = 'Основной штат сотрудников'
        verbose_name_plural = 'Основной штат сотрудников '

