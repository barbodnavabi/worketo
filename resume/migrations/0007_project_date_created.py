# Generated by Django 3.1.7 on 2021-04-26 17:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0006_auto_20210426_1004'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='date_created',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='date_created'),
            preserve_default=False,
        ),
    ]
