# Generated by Django 3.1.7 on 2021-03-21 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0003_auto_20210321_0426'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobs',
            name='experiance',
            field=models.CharField(choices=[('جونیور', 'جونیور'), ('سنیور', 'سنیور'), ('مید لول', 'مید لول'), ('مهم نیست', 'مهم نیست')], default='مهم نیست', max_length=200, verbose_name='سطح تجربه'),
        ),
    ]