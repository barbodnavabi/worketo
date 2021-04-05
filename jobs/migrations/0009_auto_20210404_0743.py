# Generated by Django 3.1.7 on 2021-04-04 14:43

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('jobs', '0008_auto_20210404_0033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobs',
            name='service',
            field=taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', related_name='services', through='jobs.Services', to='taggit.Tag', verbose_name='مسئولیت ها'),
        ),
    ]