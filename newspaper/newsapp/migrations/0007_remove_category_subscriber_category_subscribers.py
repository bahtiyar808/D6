# Generated by Django 4.2.7 on 2024-01-23 17:37

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('newsapp', '0006_remove_category_subscribers_new_category_subscriber'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='subscriber',
        ),
        migrations.AddField(
            model_name='category',
            name='subscribers',
            field=models.ManyToManyField(related_name='categories', through='newsapp.Subscriber', to=settings.AUTH_USER_MODEL),
        ),
    ]
