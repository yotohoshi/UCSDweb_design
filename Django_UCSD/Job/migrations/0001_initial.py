# Generated by Django 2.1.3 on 2018-11-26 02:01

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('User', '0001_initial'),
        ('Company', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_time', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('job_position', models.CharField(max_length=200)),
                ('type', models.CharField(choices=[('Full-time', 'Full-time'), ('Part-time', 'Part-time'), ('Contract', 'Contract'), ('Temporary', 'Temporary'), ('Commission', 'Commission'), ('Internship', 'Internship'), ('Not Available', 'Not Available')], max_length=100)),
                ('description', models.CharField(max_length=100000)),
                ('short_description', models.CharField(max_length=2000)),
                ('job_Work_Auth', models.CharField(choices=[('U.S. Citizens', 'U.S. Citizens Or U.S. Permanent Residents Only'), ('Other', 'All Legal Citizens')], max_length=100)),
                ('job_URL', models.URLField(max_length=300)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Company.Company')),
                ('degree_required', models.ManyToManyField(blank=True, to='User.Degree')),
                ('favorited_user', models.ManyToManyField(blank=True, to='User.User')),
                ('major_required', models.ManyToManyField(blank=True, to='User.Major')),
            ],
        ),
    ]
