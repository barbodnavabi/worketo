# Generated by Django 3.1.4 on 2021-03-22 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0004_jobs_experiance'),
    ]

    operations = [
        migrations.CreateModel(
            name='massage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, verbose_name='نام')),
                ('pdf', models.FileField(upload_to='pdf')),
            ],
        ),
    ]
