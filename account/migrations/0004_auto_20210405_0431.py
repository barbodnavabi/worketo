# Generated by Django 3.1.7 on 2021-04-05 11:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20210405_0426'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='avatars', verbose_name='تصویر شما'),
        ),
        migrations.AddField(
            model_name='user',
            name='is_membership',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='آکهی های ویژه'),
        ),
        migrations.AddField(
            model_name='user',
            name='special_user',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='کاربر ویژه تا'),
        ),
    ]
