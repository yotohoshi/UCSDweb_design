from django.db import models
# from django.core.exceptions import ValidationError
import django.core.validators
from django.core.exceptions import ValidationError
import Company.models
import Event.models
import uuid
from django.db.models.signals import post_save
from Registration.models import Account
from math import ceil
import string
from nltk.corpus import stopwords
from nltk.stem.porter import *
from django import forms

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
    acc = models.OneToOneField(Account, on_delete=models.CASCADE)
    UID = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    F_Name = models.CharField(max_length=20)
    L_Name = models.CharField(max_length=20)

    def __str__(self):
        return self.F_Name+" "+self.L_Name

    yr_graduation = models.IntegerField(validators=[django.core.validators.MaxValueValidator
                                                    (2050,
                                                     message='Year of graduation should be less than 2050!'),
                                                    django.core.validators.MinValueValidator(1970,
                                                    message='Year of graduation should be more than 1970!')])
    major = models.ForeignKey(Major, null=True, on_delete=models.PROTECT)
    degree = models.ForeignKey(Degree, null=True, on_delete=models.PROTECT)
    contact_email = models.EmailField( verbose_name='email address',  null=True, max_length=255, unique=True,)
    description = models.CharField(max_length=1000, validators=[django.core.validators.MinLengthValidator
                                                                (50,
                                                                 message='Description must be at least 50 characters!')])
    referral_ability = models.BooleanField
    company = models.ManyToManyField(Company.models.Company, symmetrical=False, blank=True)
    favorite_event = models.ManyToManyField(Event.models.Event, symmetrical=False, blank=True)
    friend = models.ManyToManyField('User', symmetrical=True, blank=True)
    # Getters

    # get_user_by_name
    @staticmethod
    def get_user_by_name(fname, lname):
        if type(fname) != str or type(lname) != str:
            return False
        else:
            return User.objects.all.filter(F_Name=fname, L_Name=lname)

    # get_user_by_graduation
    @staticmethod
    def get_user_by_graduation(yr_grad):
        if type(yr_grad) != int or yr_grad < 1970 or yr_grad > 2050:
            return False
        else:
             return User.objects.all.filter(yr_graduation=yr_grad)

    # get_user_by_major
    @staticmethod
    def get_user_by_major(major):
        if type(major) != Major:
            return False
        else:
            return User.objects.all.filter(Major=major)

    # get_user_by_degree
    @staticmethod
    def get_user_by_degree(degree):
        if type(degree) != Degree:
            return False
        else:
            return User.objects.all.filter(Degree=degree)

    # get_user_by_company
    @staticmethod
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
    def set_email(self, email):
        try:
            django.core.validators.validate_email(email)
            self.contact_email = email

        except ValidationError:
            return False
        return True

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
            self.company.add(comp)
            return True

    # remove_company
    def remove_company(self, comp):
        if type(comp) != Company.models.Company:
            return False
        else:
            self.company.remove(comp)
            return True

    # add_to_favorite
    def add_to_favorite(self, favorite):
        if type(favorite) != Event.models.Event:
            return False
        else:
            self.favorite_event.add(favorite)
        return True

    # remove_from_favorite
    def remove_from_favorite(self, favorite):
        if type(favorite) != Event.models.Event:
            return False
        else:
            self.favorite_event.remove(favorite)
            Event.models.Event(favorite).update_num_favorite()
        return True

    # rend_request
    def send_request(self, target):
        if type(target) != User:
            return False
        else:
            Request.objects.create(from_user=self, to_user=target)
            return True

    # accept_request
    def accept_request(self, request):
        if type(request) != Request:
            return False
        else:
            self.friend.add(request.from_user)
            request.delete()
            return True

    # deny_request
    def deny_request(self, request):
        if type(request) != Request:
            return False
        else:
            request.delete()
            return True

    # remove_friend
    def remove_friend(self, todelete):
        if type(todelete) != User:
            return False
        elif todelete in self.friend.all():
            self.friend.remove(todelete)
            return True
        else:
            return False

    # undo_request
    def undo_request(self, request):
        if type(request) != Request:
            return False
        else:
            request.delete()
            return True


class Request(models.Model):
    from_user = models.OneToOneField(User, on_delete=models.CASCADE,  related_name='+')
    to_user = models.OneToOneField(User, on_delete=models.CASCADE)


RELEVANT_COEFFICIENT = 0.5
PUNCTUATIONS = set(string.punctuation)
STOPWORDS = set(stopwords.words('english'))
STEMMER = PorterStemmer()
INFINITY = 999999


# helper method - string pre-processing
# return a list of stemmed words in the string in lowercase without punctuations, stop words, or repeated words
def string_preprocess (to_process):
    if type(to_process) != str:
        return []
    else:
        to_process = ''.join([char for char in to_process.lower() if char not in PUNCTUATIONS])
        processed = set()
        for word in to_process.split():
            if word not in STOPWORDS:
                word = STEMMER.stem(word)
                processed.add(word)
        return processed


# search_by_Keywords
def search_By_Keywords(keywords):
    if type(keywords) != str:
        return False
    else:
        # keywords pre-processing:
        keywords = string_preprocess(keywords)

        relevant_usr = []
        if len(keywords) == 0:
            threshold = INFINITY
        else:
            threshold = ceil(RELEVANT_COEFFICIENT * len(keywords))

        for usr in User.objects.all():

            # description pre-processing
            full_name = usr.__str__()
            full_name = string_preprocess(full_name)

            # comparing keywords with job descriptions
            counter = 0
            for word in keywords:
                if word in full_name:
                    counter += 1

                if counter >= threshold:
                    relevant_usr.append(usr)
        return relevant_usr
