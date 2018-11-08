from django.db import models
# from django.core.exceptions import ValidationError
import django.core.validators
import Company.models
import Event.models
import uuid

# Create your models here.

""" User Class
    This Class Defines a user entity. 
    Constructor: Populate the User table with given parameters
"""


class Major(models.Model):
    db_table = 'Majors',
    major = models.CharField(max_length=50, primary_key=True)


class Degree(models.Model):
    db_table = 'Degrees'

    # FIXME : Multiple choice field can't be set as primary key.
    ''' 
    DEGREE_CHOICES = (
        ('BS', 'BS'),
        ('BA', 'BA'),
        ('MS', 'MS'),
        ('MA', 'MA'),
        ('Ph.D', 'Ph.D'),
    )'''
    degree = models.CharField(max_length=3, primary_key=True)


# Getters
# get_Major() TODO


# get_Degree() TODO


class User(models.Model):
    db_table = 'user',
    UID = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    F_Name = models.CharField(max_length=20)
    L_Name = models.CharField(max_length=20)
    yr_graduation = models.IntegerField(validators=[django.core.validators.MaxValueValidator
                                                                  (2050,
                                                                message='Year of graduation should be less than 2050!'),
                                                                  django.core.validators.MinValueValidator(1970,
                                                                message='Year of graduation should be more than 1970!')])
    major = models.ForeignKey(Major,  on_delete=models.PROTECT)
    degree = models.ForeignKey(Degree, on_delete=models.PROTECT)
    contact_email = models.CharField(max_length=60, unique=True, validators=[django.core.validators.EmailValidator
                                                                  (message='Please Use a valid email address!',
                                                                   code=None, whitelist=None)])
    description = models.CharField(max_length=300)
    referral_ability = models.BooleanField
    company = models.ManyToManyField(Company.models.Company, symmetrical=False, blank=True)
    # Originally from registration app
    register_email = models.CharField(max_length=60, unique=True, validators=[django.core.validators.EmailValidator
                                                                  (message='Please Use a valid email address!',
                                                                   code=None, whitelist=None)])
    password = models.CharField(max_length=20, validators=[django.core.validators.MinLengthValidator
                                                           (8, message='Password must be at least 8 characters!')])
    # Re-implemented favorite table
    favorite_event = models.ManyToManyField(Event.models.Event, symmetrical=False, blank=True)

# Getters
# get_UID() TODO


# get_Name() TODO


# get_Graduation() TODO


# get_Description() TODO


# get_Company() TODO


# Deleted favorite table, using many-to-many relationship instead
'''
    class Favorite(models.Model):
    db_table = 'Favorite',
    Usr = models.ForeignKey(User, on_delete=models.PROTECT)
    Event = models.ForeignKey(Event.models.Events, on_delete=models.PROTECT)
'''

