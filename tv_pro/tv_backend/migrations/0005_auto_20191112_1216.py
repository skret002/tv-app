# Generated by Django 2.2.7 on 2019-11-12 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tv_backend', '0004_auto_20191112_1157'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='home',
            name='slider',
        ),
        migrations.AddField(
            model_name='home',
            name='slider',
            field=models.ManyToManyField(related_name='slide', to='tv_backend.SlideInHome'),
        ),
    ]
