# Generated by Django 2.1.4 on 2018-12-08 07:12

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
