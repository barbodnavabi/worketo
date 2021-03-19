# Generated by Django 3.1.7 on 2021-03-19 14:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('services', models.CharField(max_length=300, verbose_name='jobs')),
            ],
        ),
        migrations.RenameField(
            model_name='jobs',
            old_name='tags',
            new_name='important',
        ),
        migrations.AddField(
            model_name='jobs',
            name='Type',
            field=models.CharField(choices=[('d', 'دور کاری'), ('t', 'تمام وقت'), ('n', 'پاره وقت'), ('p', 'پروژه ای')], default='d', max_length=1, verbose_name='وضعیت شغلی'),
        ),
        migrations.AddField(
            model_name='jobs',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='account.user', verbose_name='نویسنده'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='jobs',
            name='price',
            field=models.PositiveIntegerField(default=1, verbose_name='حقوق'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='jobs',
            name='soldiering',
            field=models.CharField(choices=[('p', 'معاف یا پایان خدمت'), ('i', 'مهم نیست')], default='i', max_length=1, verbose_name='وضعیت نظام وظیفه'),
        ),
        migrations.AddField(
            model_name='jobs',
            name='status',
            field=models.CharField(choices=[('p', 'منتشر شده'), ('i', 'در حال بررسی'), ('b', 'منقضی شده')], default='i', max_length=1, verbose_name='وضعیت'),
        ),
        migrations.CreateModel(
            name='Cities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='نام استان')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='آدرس استان')),
                ('status', models.BooleanField(default=True, verbose_name='آیا نمایش داده شود؟')),
                ('position', models.IntegerField(verbose_name='پوزیشن')),
                ('parent', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='children', to='jobs.cities', verbose_name='زیردسته')),
            ],
            options={
                'verbose_name': 'دسته\u200cبندی',
                'verbose_name_plural': 'دسته\u200cبندی ها',
                'ordering': ['parent__id', 'position'],
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='عنوان دسته\u200cبندی')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='آدرس دسته\u200cبندی')),
                ('status', models.BooleanField(default=True, verbose_name='آیا نمایش داده شود؟')),
                ('position', models.IntegerField(verbose_name='پوزیشن')),
                ('parent', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='children', to='jobs.category', verbose_name='زیردسته')),
            ],
            options={
                'verbose_name': 'دسته\u200cبندی',
                'verbose_name_plural': 'دسته\u200cبندی ها',
                'ordering': ['parent__id', 'position'],
            },
        ),
        migrations.AddField(
            model_name='jobs',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='jobs.category', verbose_name='دسته بندی'),
        ),
        migrations.AddField(
            model_name='jobs',
            name='city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='jobs.cities', verbose_name='شهر'),
        ),
        migrations.AddField(
            model_name='jobs',
            name='services',
            field=models.ManyToManyField(to='jobs.Services', verbose_name='وظایف'),
        ),
    ]
