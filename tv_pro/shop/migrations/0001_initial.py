# Generated by Django 3.0 on 2020-06-04 09:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, verbose_name='Название категории')),
            ],
            options={
                'verbose_name': 'Категория запчасти',
                'verbose_name_plural': 'Категории для запчастей',
                'db_table': 'CategoryShop',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='OrderShop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_status', models.CharField(choices=[('0', 'Ждет обработки'), ('1', 'Отправлен в ригион'), ('2', 'Выдан курьеру'), ('3', 'Завершен')], default=0, max_length=1, verbose_name='Статус Заказа')),
                ('delivery_status', models.CharField(choices=[('0', 'Доставка по СПБ'), ('1', 'Отправить в регион'), ('2', 'Самовывоз')], default=0, max_length=1, verbose_name='Тип доставки')),
                ('name', models.CharField(blank=True, max_length=100, verbose_name='Имя')),
                ('phone', models.CharField(blank=True, max_length=100, verbose_name='Телефон')),
                ('address', models.CharField(blank=True, max_length=150, null=True, verbose_name='адрес')),
            ],
            options={
                'verbose_name': 'Заказ с Магазина',
                'verbose_name_plural': 'Заказы с магазина',
                'db_table': 'OrderShop',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Parts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, verbose_name='Название запчасти')),
                ('price', models.IntegerField(blank=True, verbose_name='Цена запчасти')),
                ('stock', models.CharField(choices=[('0', 'В наличии'), ('1', 'Товара нет в наличии'), ('2', 'Скоро появится в продаже')], default=1, max_length=1, verbose_name='В наличии?')),
                ('delivery_of_spb', models.IntegerField(blank=True, default=500, verbose_name='Цена доставки по СПБ')),
                ('delivery_of_region', models.BooleanField(blank=True, default=True, verbose_name='можем ли отправить в регион')),
                ('status_part', models.CharField(choices=[('0', 'БУ'), ('1', 'НОВЫЙ'), ('2', 'Под восстановление')], max_length=1, verbose_name='Состояние товара')),
                ('guarantee', models.CharField(choices=[('1 день на проверку', '1 день на проверку'), ('нет', 'нет'), ('3 дня', '3 дня'), ('14 дней', '14 дней'), ('30 дней', '30 дней')], default='1 день на проверку', max_length=25, verbose_name='Гарантия')),
                ('f_img', models.CharField(max_length=300, null=True, verbose_name='Основное фото')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Category')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.OrderShop')),
            ],
            options={
                'verbose_name': 'Запчасть',
                'verbose_name_plural': 'Запчасти',
                'db_table': 'Parts',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='PartsImg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='./parts_img/', verbose_name='Фото запчасти')),
                ('parts', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Parts')),
            ],
            options={
                'verbose_name': 'Фото',
                'verbose_name_plural': 'Фотографии',
                'db_table': 'PartsImg',
                'managed': True,
            },
        ),
    ]
