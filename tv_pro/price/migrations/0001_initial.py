# Generated by Django 3.0 on 2020-01-13 22:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LogoTv',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flag', models.CharField(blank=True, max_length=25, verbose_name='подпись логотипа')),
                ('logo_brend', models.ImageField(upload_to='./logo_brend/', verbose_name='логотип бренда')),
            ],
            options={
                'verbose_name': 'Логотип бренда',
                'verbose_name_plural': 'Логотипы брендов',
            },
        ),
        migrations.CreateModel(
            name='Malfunks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('malfunk', models.CharField(choices=[('1', 'статья 1'), ('2', 'статья 6'), ('3', 'статья 5'), ('4', 'статья внутри 4'), ('5', 'статья 2'), ('6', 'статья 3')], max_length=100, verbose_name='Тип неисправности')),
            ],
            options={
                'verbose_name': 'Тип неисправности',
                'verbose_name_plural': 'Типы неисправностей',
            },
        ),
        migrations.CreateModel(
            name='NameBrend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brend_name', models.CharField(blank=True, max_length=75)),
                ('logo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='price.LogoTv', verbose_name='Выбрать логотип')),
            ],
            options={
                'verbose_name': 'Имя брендов',
                'verbose_name_plural': 'Имена брендов',
            },
        ),
        migrations.CreateModel(
            name='TypeLcd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_lcd', models.CharField(blank=True, max_length=150, verbose_name='Тип аппарата (монитор, жк, плазма)')),
                ('type_lcd_img', models.ImageField(upload_to='./type_lcd_img/', verbose_name='Тип апарата наглядно+')),
            ],
            options={
                'verbose_name': 'Тип аппарата',
                'verbose_name_plural': 'Тип аппарата',
            },
        ),
        migrations.CreateModel(
            name='TvSizePrice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(blank=True, max_length=150, verbose_name='Диаганаль телевизора')),
                ('price', models.CharField(blank=True, max_length=50)),
                ('malfunk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='price.Malfunks', verbose_name='malfunk')),
            ],
            options={
                'verbose_name': 'Диаганаль телевизора',
                'verbose_name_plural': 'Диаганали телевизоров',
            },
        ),
        migrations.CreateModel(
            name='TvBrend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brend_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='price.NameBrend', verbose_name='Имя бренда')),
                ('type_lcd', models.ManyToManyField(to='price.TypeLcd', verbose_name='тип аппарата')),
            ],
            options={
                'verbose_name': 'Бренд телевизора',
                'verbose_name_plural': 'Бренды телевизоров',
            },
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brend_size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='price.TvBrend', verbose_name='выбрать аппарат')),
            ],
            options={
                'verbose_name': 'Аппарат, неисправность и цена',
                'verbose_name_plural': 'Аппараты, неисправности и цены',
            },
        ),
        migrations.AddField(
            model_name='malfunks',
            name='price',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='price.Price', verbose_name='Девайс и его параметры'),
        ),
    ]
