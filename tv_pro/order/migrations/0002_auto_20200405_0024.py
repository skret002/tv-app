# Generated by Django 3.0 on 2020-04-04 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='time_call',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Звонить в'),
        ),
    ]