# Generated by Django 3.0 on 2020-04-29 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0002_auto_20200429_1602'),
    ]

    operations = [
        migrations.RenameField(
            model_name='staff',
            old_name='staff',
            new_name='video',
        ),
        migrations.AlterField(
            model_name='aboutstaff',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='./video_staff', verbose_name='видео на стр. о сотрудниках'),
        ),
    ]