# Generated by Django 2.1.3 on 2018-11-21 04:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0003_auto_20181120_2043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='major',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='User.Major'),
        ),
    ]
