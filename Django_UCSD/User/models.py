from django.db import models
# from django.core.exceptions import ValidationError
import django.core.validators
from django.core.exceptions import ValidationError
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
    major = models.ForeignKey(Major, on_delete=models.PROTECT)
    degree = models.ForeignKey(Degree, on_delete=models.PROTECT)
    contact_email = models.CharField(max_length=60, unique=True, validators=[django.core.validators.EmailValidator
        (
        message='Please Use a valid email address!',
        code=None, whitelist=None)])
    description = models.CharField(max_length=1000, validators=[django.core.validators.MinLengthValidator
                                                                (50,
                                                                 message='Description must be at least 50 characters!')])
    referral_ability = models.BooleanField
    company = models.ManyToManyField(Company.models.Company, symmetrical=False, blank=True)
    # Originally from registration app
    register_email = models.CharField(max_length=60, unique=True, validators=[django.core.validators.EmailValidator
        (
        message='Please Use a valid email address!',
        code=None, whitelist=None)])
    password = models.CharField(max_length=20, validators=[django.core.validators.MinLengthValidator
                                                           (8, message='Password must be at least 8 characters!')])
    # Re-implemented favorite table
    favorite_event = models.ManyToManyField(Event.models.Event, symmetrical=False, blank=True)


# Getters


# get_user_by_name


def get_user_by_name(fname, lname):
    if type(fname) != str or type(lname) != str:
        return False
    else:
        return User.objects.all.filter(F_Name=fname, L_Name=lname)


# get_user_by_graduation


def get_user_by_graduation(yr_grad):
    if type(yr_grad) != int or yr_grad < 1970 or yr_grad > 2050:
        return False
    else:
        return User.objects.all.filter(yr_graduation=yr_grad)


# get_user_by_major


def get_user_by_major(major):
    if type(major) != Major:
        return False
    else:
        return User.objects.all.filter(Major=major)


# get_user_by_degree


def get_user_by_degree(degree):
    if type(degree) != Degree:
        return False
    else:
        return User.objects.all.filter(Degree=degree)


# get_user_by_company

def get_user_by_company(company):
    if type(company) != Company.models.Company:
        return False
    else:
        return User.objects.all.filter(Company=company)


# Setter

# set_fame


def set_fname(self, fname):
    if type(fname) != str:
        return False
    else:
        self.F_Name = fname
        return True


# set_lname


def set_lname(self, lname):
    if type(lname) != str:
        return False
    else:
        self.L_Name = lname
        return True


# set_yr_grad


def set_yr_grad(self, yr_grad):
    if type(yr_grad) != int or yr_grad < 1970 or yr_grad > 2050:
        return False
    else:
        self.yr_graduation = yr_grad
        return True


# set_major


def set_major(self, majr):
    if type(majr) != Major:
        return False
    else:
        self.major = majr
        return True


# set_degree


def set_degree(self, deg):
    if type(deg) != Degree:
        return False
    else:
        self.degree = deg
        return True


# set_email


def set_email(self, email, kind):
    try:
        django.core.validators.validate_email(email)
        if kind == 0:
            self.contact_email = email
            return True
        elif kind == 1:
            self.register_email = email
            return True
        else:
            return False
    except ValidationError:
        return False


# set_description


def set_description(self, descrip):
    if type(descrip) != str or len(descrip) > 300 or len(descrip) < 50:
        return False
    else:
        self.description = descrip
        return True


# add_company


def add_company(self, comp):
    if type(comp) != Company.models.Company:
        return False
    else:
        self.companys.add(comp)
        return True


# remove_company


def remove_company(self, comp):
    if type(comp) != Company.models.Company:
        return False
    else:
        self.companys.remove(comp)
        return True


# add_to_favorite


def add_to_favorite(self, favorite):
    if type(favorite) != Event.models.Event:
        return False
    else:
        self.favorite_events.add(favorite)
    return True


# remove_from_favorite


def remove_from_favorite(self, favorite):
    if type(favorite) != Event.models.Event:
        return False
    else:
        self.favorite_events.remove(favorite)
        Event.models.Event(favorite).update_num_favorite()
    return True


# change_password TODO


# Deleted favorite table, using many-to-many relationship instead
'''
    class Favorite(models.Model):
    db_table = 'Favorite',
    Usr = models.ForeignKey(User, on_delete=models.PROTECT)
    Event = models.ForeignKey(Event.models.Events, on_delete=models.PROTECT)
'''
