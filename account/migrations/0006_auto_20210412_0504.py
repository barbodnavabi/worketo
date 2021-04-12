# Generated by Django 3.1.7 on 2021-04-12 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_auto_20210405_0933'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='facebook',
            field=models.URLField(blank=True, null=True, verbose_name='لینک فیسبوک'),
        ),
        migrations.AddField(
            model_name='user',
            name='github',
            field=models.URLField(blank=True, null=True, verbose_name='لینک گیتهاب'),
        ),
        migrations.AddField(
            model_name='user',
            name='instagram',
            field=models.URLField(blank=True, null=True, verbose_name='لینک اینستاگرام'),
        ),
        migrations.AddField(
            model_name='user',
            name='linkendin',
            field=models.URLField(blank=True, null=True, verbose_name='لینکندین'),
        ),
        migrations.AddField(
            model_name='user',
            name='telegram',
            field=models.URLField(blank=True, null=True, verbose_name='تلگرام'),
        ),
        migrations.AddField(
            model_name='user',
            name='whatsApp',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='واتساپ'),
        ),
    ]
