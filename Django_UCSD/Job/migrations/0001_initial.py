<<<<<<< HEAD
# Generated by Django 2.1.3 on 2018-11-15 11:26
=======
# Generated by Django 2.1.2 on 2018-11-15 09:24
>>>>>>> master

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
<<<<<<< HEAD
        ('Company', '0002_auto_20181114_0519'),
        ('User', '0001_initial'),
=======
        ('User', '0001_initial'),
        ('Company', '0002_auto_20181114_0519'),
>>>>>>> master
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('JobID', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('job_position', models.CharField(max_length=200)),
                ('type', models.IntegerField(validators=[django.core.validators.MaxValueValidator(1, message=None), django.core.validators.MinValueValidator(0, message=None)])),
                ('description', models.CharField(max_length=300)),
                ('job_URL', models.URLField(max_length=300)),
                ('job_duration', models.CharField(max_length=100)),
                ('job_location', models.CharField(max_length=100)),
                ('job_Work_Auth', models.CharField(choices=[('U.S Citizen', 'U.S Citizen'), ('Permanent Resident', 'Permanent Resident'), ('F-1', 'F-1'), ('H1-B', 'H1-B'), ('Otherwise', 'Otherwise Authorized to Work')], max_length=100)),
                ('Degree_Require', models.ManyToManyField(blank=True, to='User.Degree')),
                ('Major_Require', models.ManyToManyField(blank=True, to='User.Major')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Company.Company')),
            ],
        ),
    ]