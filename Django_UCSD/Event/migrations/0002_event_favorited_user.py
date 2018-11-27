# Generated by Django 2.1.3 on 2018-11-26 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0002_remove_user_favorite_event'),
        ('Event', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='favorited_user',
            field=models.ManyToManyField(blank=True, to='User.User'),
        ),
    ]
