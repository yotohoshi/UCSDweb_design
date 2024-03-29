# Generated by Django 2.1.4 on 2018-12-08 13:58

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Company', '0001_initial'),
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=150)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('location', models.CharField(max_length=100)),
                ('type', models.IntegerField(validators=[django.core.validators.MaxValueValidator(1), django.core.validators.MinValueValidator(0)])),
                ('description', models.CharField(default='This event have no descriptions yet.', max_length=1000)),
                ('num_views', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('num_favorites', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Company.Company')),
                ('favorited_user', models.ManyToManyField(blank=True, to='User.User')),
                ('go_user', models.ManyToManyField(blank=True, related_name='go', to='User.User')),
            ],
        ),
    ]
