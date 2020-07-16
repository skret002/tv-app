# Generated by Django 3.0 on 2020-06-07 19:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_productinorder'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productinorder',
            name='total_price',
        ),
        migrations.AddField(
            model_name='productinorder',
            name='count',
            field=models.IntegerField(default=1, verbose_name='Кол-во в заказе'),
        ),
        migrations.AlterField(
            model_name='productinorder',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Подтвержден'),
        ),
        migrations.AlterField(
            model_name='productinorder',
            name='product',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.Parts', verbose_name='Товар'),
        ),
    ]