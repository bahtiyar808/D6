# Generated by Django 4.2.7 on 2024-01-23 17:20

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('newsapp', '0003_category_subscribers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='subscribers',
            field=models.ManyToManyField(related_name='categories', through='newsapp.Subscriber', to=settings.AUTH_USER_MODEL),
        ),
    ]
