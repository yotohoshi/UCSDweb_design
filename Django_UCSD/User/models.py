from django.db import models
import django.core.validators
from django.core.exceptions import ValidationError
import Company.models
from Registration.models import Account
from math import ceil
import string
from nltk.corpus import stopwords
from nltk.stem.porter import *
from random import *
from datetime import date

############################################# Helper Functions ##########################################
GARYID = 2

############################################# Models ###################################################


class Major(models.Model):
    db_table = 'Majors',
    major = models.CharField(max_length=50, primary_key=True)

    @staticmethod
    def getMajorList():
        return [dic['major'] for dic in Major.objects.values('major')]


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
    degree = models.CharField(max_length=15, primary_key=True)

    @staticmethod
    def getDegreeList():
        return [dic['degree'] for dic in Degree.objects.values('degree')]


class User(models.Model):
    db_table = 'user',
    acc = models.OneToOneField(Account, on_delete=models.CASCADE, null=True)
    F_Name = models.CharField(max_length=20)
    L_Name = models.CharField(max_length=20)
   # p_id = models.CharField(max_length=1500)
    # ProfilePic = models.ImageField(upload_to='profile_image', blank=True, default='profile_image/File_Pikachu.png')
    yr_graduation = models.IntegerField(validators=[django.core.validators.MaxValueValidator(2050, message='Year of graduation should be less than 2050!'),
                                                    django.core.validators.MinValueValidator(1970, message='Year of graduation should be more than 1970!')])
    major = models.ForeignKey(Major, null=True, on_delete=models.PROTECT)
    degree = models.ForeignKey(Degree, null=True, on_delete=models.PROTECT)
    contact_email = models.EmailField(verbose_name='email address', null=True, max_length=255, unique=True)
    description = models.CharField(max_length=1500,
                                   validators=[django.core.validators.MinLengthValidator(50, message='Description must be at least 50 characters!')])
    referral_ability = models.BooleanField(default=False)
    company = models.ForeignKey(Company.models.Company, on_delete=models.PROTECT, null=True, blank=True)
    friend = models.ManyToManyField('User', symmetrical=True, blank=True)
    recommended_users = models.ManyToManyField('User', symmetrical=False, blank=True)
    picdata = models.CharField(max_length=256000)


    ################################################################## Getters


    # define the string representation of the user objects
    def __str__(self):
        return self.F_Name + " " + self.L_Name

    # get the number of common friends between two users
    # parameters user1 and user2 are user objects
    @staticmethod
    def get_common_friend_number(user1, user2):
        if type(user1) != User or type(user2) != User:
            return False
        user1Friends = set(user1.friend.all())
        user2Friends = set(user2.friend.all())
        return len(user1Friends.intersection(user2Friends))

    # get the referral list of a user
    # parameter user is an automatically generated user object id
    @staticmethod
    def get_referral_list(userId):
        try:
            user = User.objects.get(id=userId)
        except:
            return False

        referralList = []
        for pal in user.friend.all():
            if pal.referral_ability:
                referralList.append(pal)
        if user.referral_ability:
            referralList.append(user)
        return referralList

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


    ################################################################## Setter


    # set a user's 'friends who has common friends with the user' list
    # parameter user is a user object
    @staticmethod
    def set_recommended_list(user):
        if type(user) != User:
            return False

        for pal in user.friend.all():
            if len(set(user.friend.all()).intersection(set(pal.friend.all()))) != 0:
                user.recommended_users.add(pal)

        num_of_users = User.objects.all().count()
        # if the total number user is smaller than 5, add all users to his recommended list
        if num_of_users < 5:
            for pal in User.objects.all():
                if pal != user:
                    user.recommended_users.add(pal)
        else:
            while len(user.recommended_users.all()) < 5:
                index = randint(0, num_of_users - 1)
                user.recommended_users.add(User.objects.all()[index])
        return True

    # set_fname
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

    # send_request
    def send_request(self, target):
        if type(target) != User:
            return False
        else:
            if not Request.objects.filter(from_user=self).filter(to_user=target):
                request = Request(from_user=self, to_user=target)
                request.save()
                print('dd')
                if target == User.get_gary():
                    target.accept_request(request)
                return True
            else:
                return False

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

    # update_user_info
    def update_user_info(self, major, degree, contact_email, description, year_graduation, company):
        if major:
            major_obj = list(Major.objects.filter(major=major))[0]
            self.major = major_obj
        if degree:
            degree_obj = list(Degree.objects.filter(degree=degree))[0]
            self.degree = degree_obj
        if contact_email:
            self.contact_email = contact_email
        if description:
            self.description = description
        if year_graduation:
            self.yr_graduation = year_graduation
        if company:
            company_obj = list(Company.models.Company.objects.filter(company_name=company))[0]
            self.company = company_obj
        self.save()
        return True

    # get_go_events
    def get_go_events_today(self):
        return self.go.filter(date=date.today()).order_by('time')

    # This function is for demonstration purposes
    # get_gary
    @staticmethod
    def get_gary():
        return list(User.objects.filter(id=GARYID))[0]

    # gary_send_request
    @staticmethod
    def gary_send_request(user):
        print('db')
        gary = User.get_gary()
        if gary.send_request(user):
            return True
        else:
            return False


class Request(models.Model):
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_request')
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_request')


RELEVANT_COEFFICIENT = 0.5
PUNCTUATIONS = set(string.punctuation)
STOPWORDS = set(stopwords.words('english'))
STEMMER = PorterStemmer()
INFINITY = 999999


# helper method - string pre-processing
# return a list of stemmed words in the string in lowercase without punctuations, stop words, or repeated words
def string_preprocess(to_process):
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
