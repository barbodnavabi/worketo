# Generated by Django 3.1.7 on 2021-04-26 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0005_auto_20210426_1004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='percent',
            field=models.DecimalField(decimal_places=0, max_digits=4, verbose_name='چند درصد در این مهارت حرفه ای هستید؟'),
        ),
    ]
