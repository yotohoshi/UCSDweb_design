# Generated by Django 2.1.4 on 2018-12-08 13:58

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Anonymous',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('ip', models.CharField(max_length=200, unique=True)),
                ('last_searched_keyword', models.CharField(blank=True, default=None, max_length=1000, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('account_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('last_searched_keyword', models.CharField(blank=True, default=None, max_length=1000, null=True)),
                ('last_searched_location', models.CharField(blank=True, default=None, max_length=1000, null=True)),
                ('is_new_user', models.BooleanField(default=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
