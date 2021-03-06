# Generated by Django 3.1.7 on 2021-03-21 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_auto_20210320_1633'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cities',
            options={'ordering': ['parent__id', 'position'], 'verbose_name': 'شهر', 'verbose_name_plural': 'شهر ها'},
        ),
        migrations.AlterField(
            model_name='jobs',
            name='price',
            field=models.CharField(choices=[('توافقی', 'توافقی'), ('2 تا 3 میلیون', '2 تا 3 میلیون'), ('8 تا 9 میلیون', '8 تا 9 میلیون'), ('10 تا 12 میلیون', '10 تا 12 میلیون'), ('12 تا 20 میلیون', '12 تا 20 میلیون'), ('دیگر قیمت ها', 'دیگر قیمت ها')], default='12 تا 20 میلیون', max_length=200, verbose_name='حقوق'),
        ),
    ]
