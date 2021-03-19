# Generated by Django 3.1.7 on 2021-03-19 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='Employee',
            field=models.BooleanField(default=False, verbose_name='آیا کارجو هستید؟'),
        ),
        migrations.AddField(
            model_name='user',
            name='employer',
            field=models.BooleanField(default=False, verbose_name='آیا کارفرما هستید؟'),
        ),
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.CharField(default=1, max_length=12, unique=True, verbose_name='تلفن'),
            preserve_default=False,
        ),
    ]
