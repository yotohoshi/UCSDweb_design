<<<<<<< HEAD
# Generated by Django 2.1.3 on 2018-11-25 11:29
=======
# Generated by Django 2.1.3 on 2018-11-25 09:42
>>>>>>> master

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Company', '0001_initial'),
        ('Event', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Degree',
            fields=[
                ('degree', models.CharField(max_length=3, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Major',
            fields=[
                ('major', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('UID', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('F_Name', models.CharField(max_length=20)),
                ('L_Name', models.CharField(max_length=20)),
                ('yr_graduation', models.IntegerField(validators=[django.core.validators.MaxValueValidator(2050, message='Year of graduation should be less than 2050!'), django.core.validators.MinValueValidator(1970, message='Year of graduation should be more than 1970!')])),
                ('contact_email', models.EmailField(max_length=255, null=True, unique=True, verbose_name='email address')),
                ('description', models.CharField(max_length=1000, validators=[django.core.validators.MinLengthValidator(50, message='Description must be at least 50 characters!')])),
                ('acc', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('company', models.ManyToManyField(blank=True, to='Company.Company')),
                ('degree', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='User.Degree')),
                ('favorite_event', models.ManyToManyField(blank=True, to='Event.Event')),
                ('friend', models.ManyToManyField(blank=True, related_name='_user_friend_+', to='User.User')),
                ('major', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='User.Major')),
            ],
        ),
        migrations.AddField(
            model_name='request',
            name='from_user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='User.User'),
        ),
        migrations.AddField(
            model_name='request',
            name='to_user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='User.User'),
        ),
    ]
