# Generated by Django 3.0 on 2020-06-07 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_auto_20200607_2225'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordershop',
            name='total_price',
            field=models.IntegerField(default=0, verbose_name='Общая сумма заказа'),
            preserve_default=False,
        ),
    ]
