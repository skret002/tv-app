# Generated by Django 3.0 on 2020-04-28 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tv_backend', '0011_reviews'),
    ]

    operations = [
        migrations.AlterField(
            model_name='typesofmalfunctions',
            name='content',
            field=models.TextField(blank=True, max_length=500, verbose_name='Контент'),
        ),
    ]
