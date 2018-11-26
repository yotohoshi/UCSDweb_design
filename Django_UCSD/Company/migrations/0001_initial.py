# Generated by Django 2.1.3 on 2018-11-26 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('company_name', models.CharField(max_length=100, primary_key=True, serialize=False, unique=True)),
                ('description', models.CharField(default='This company have no descriptions yet.', max_length=300)),
            ],
        ),
    ]
