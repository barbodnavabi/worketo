# Generated by Django 3.1.7 on 2021-04-04 07:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0007_auto_20210322_0537'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jobs',
            old_name='city',
            new_name='state',
        ),
    ]
