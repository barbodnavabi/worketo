# Generated by Django 3.1.7 on 2021-03-20 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0005_auto_20210320_1009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobs',
            name='Type',
            field=models.CharField(choices=[('d', 'دور کاری'), ('t', 'تمام وقت'), ('n', 'پاره وقت'), ('k', 'کارآموزی'), ('p', 'پروژه ای')], default='d', max_length=200, verbose_name='وضعیت شغلی'),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='price',
            field=models.CharField(choices=[('p', 'توافقی'), ('b', '2 تا 3 میلیون'), ('i', '8 تا 9 میلیون'), ('s', '10 تا 12 میلیون'), ('c', '12 تا 20 میلیون'), ('o', 'دیگر قیمت ها')], default='i', max_length=200, verbose_name='حقوق'),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='soldiering',
            field=models.CharField(choices=[('معاف', 'معاف'), ('پایان خدمت', 'پایان خدمت'), ('مهم نیست', 'مهم نیست')], default='مهم نیست', max_length=200, verbose_name='وضعیت نظام وظیفه'),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='status',
            field=models.CharField(choices=[('p', 'منتشر شده'), ('i', 'در حال بررسی'), ('b', 'منقضی شده')], default='i', max_length=200, verbose_name='وضعیت'),
        ),
    ]