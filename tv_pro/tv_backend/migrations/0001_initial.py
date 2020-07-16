# Generated by Django 2.2.7 on 2019-11-11 19:05

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(blank=True, max_length=12)),
                ('adress', models.CharField(blank=True, max_length=50)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('time_work', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='SlideInHome',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slaid_title', models.CharField(blank=True, max_length=50)),
                ('content', tinymce.models.HTMLField(blank=True, max_length=500)),
            ],
        ),
    ]
