import uuid
from datetime import datetime

import django.core.validators
from django.db import models
from Category.models import Category
import Company.models
from User.models import Major, Degree, User
import string
from math import ceil
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import *
from nltk.stem import WordNetLemmatizer
import time


#################################### Constants #######################################################


WORKAUTHS = (
    ('U.S. Citizens', 'U.S. Citizens Or U.S. Permanent Residents Only'),
    ('Other', 'All Legal Citizens'),
)

JOBTYPES = (
    ('Full-time', 'Full-time'),
    ('Part-time', 'Part-time'),
    ('Contract', 'Contract'),
    ('Temporary', 'Temporary'),
    ('Commission', 'Commission'),
    ('Internship', 'Internship'),
    ('Not Available', 'Not Available')
)
PUNCTUATIONS = set(string.punctuation)
STOPWORDS = set(stopwords.words('english'))
STEMMER = PorterStemmer()
LEMMATIZER = WordNetLemmatizer()
RELEVANT_COEFFICIENT = 0.7
INFINITY = 999999
# CATEGORYKEYWORDS = {'software': 'S',
#                     'hardware': 'H',
#                     'embedded': 'EM',
#                     'art': 'AR',
#                     'business': 'B',
#                     'math': 'M',
#                     'accounting': 'AC',
#                     'physics': 'PHY',
#                     'communication': 'COMM',
#                     'computer': 'C',
#                     'science': 'SC',
#                     'music': 'MUS',
#                     'biology': 'BIO',
#                     'bioengineering': 'BE',
#                     'chemistry': 'CHEM',
#                     'electrical': 'ELE',
#                     'biochemistry': 'BC',
#                     'laborer': 'L',
#                     'labor': 'L'}

CATEGORYKEYWORDS = {'softwar': 'S',
                    'hardwar': 'H',
                    'embed': 'EM',
                    'art': 'AR',
                    'busi': 'B',
                    'math': 'M',
                    'account': 'AC',
                    'physic': 'PHY',
                    'commun': 'COMM',
                    'comput': 'C',
                    'scienc': 'SC',
                    'music': 'MUS',
                    'biolog': 'BIO',
                    'bioengin': 'BE',
                    'chemistri': 'CHEM',
                    'electr': 'ELE',
                    'biochemistri': 'BC',
                    'labor': 'L'}


TABLE = {9: 32, 33: 32, 34: 32, 35: 32, 36: 32, 37: 32, 38: 32, 39: 32, 40: 32, 41: 32, 42: 32,
         43: 32, 44: 32, 45: 32, 46: 32, 47: 32, 58: 32, 59: 32, 60: 32, 61: 32, 62: 32, 63: 32,
         64: 32, 91: 32, 92: 32, 93: 32, 94: 32, 95: 32, 96: 32, 123: 32, 124: 32, 125: 32, 126: 32}


##################################### Helper Methods ######################################################


# helper method - string pre-processing
# return a set of stemmed words in the string in lowercase without punctuations, stop words, or repeated words
def string_preprocess (to_process):
    if type(to_process) != str:
        return []
    else:
        #to_process = to_process.lower().translate(TABLE).split()
        to_process = ''.join([char for char in to_process.lower() if char not in PUNCTUATIONS]).split()
        processed = set()
        for word in to_process:
            if word not in STOPWORDS:
                word = STEMMER.stem(word)
                #LEMMATIZER.lemmatize(word)
                processed.add(word)
        return processed


def performance(to_run):
    start = time.time()
    to_run
    end = time.time()
    print(end - start)

##################################### Models ################################################################


class Location(models.Model):
    place = models.CharField(primary_key=True, max_length=100)

    def __str__(self):
        return self.place


class Job(models.Model):
    db_table = 'Job'
    post_time = models.DateTimeField(default=datetime.now, blank=True)

    # from data
    job_position = models.CharField(max_length=200)
    type = models.CharField(max_length=100, choices=JOBTYPES)
    description = models.CharField(max_length=100000)
    short_description = models.CharField(max_length=2000)
    degree_required = models.ManyToManyField(Degree, blank=True)
    major_required = models.ManyToManyField(Major, blank=True)
    job_Work_Auth = models.CharField(max_length=100, choices=WORKAUTHS)
    company = models.ForeignKey(Company.models.Company, on_delete=models.PROTECT)
    job_URL = models.URLField(max_length=300)
    favorited_user = models.ManyToManyField(User, blank=True, symmetrical=False)
    category = models.ManyToManyField(Category, blank=True)
    num_views = models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])
    location = models.ForeignKey(Location, on_delete=models.PROTECT)
    paid = models.BooleanField(default=True)

    @staticmethod
    def general_Search(keywords, work_auth, degs, location, pay, tp):

        # parameter keywords is a string. detect implied categories in the keywords and filter by category
        if keywords is not None:
            # keywords pre-processing:
            keywords = list(string_preprocess(keywords))

            # category detection
            categories = set()
            for word in keywords:
                if word in CATEGORYKEYWORDS:
                    categories.add(CATEGORYKEYWORDS[word])
            categories = list(categories)
            if len(categories) == 0:
                result = Job.objects.all()
            else:
                result = Job.objects.filter(category__in=list(categories))

        # parameter work_auth is an array of strings
        if work_auth is not None:
            result = result.filter(job_Work_Auth__in=work_auth)

        # parameter degs is an array of strings
        if degs is not None:
            result = result.filter(degree_required__in=degs)

        # parameter location is a string
        if location is not None:
            result = result.filter(location__in=[location])

        # parameter pay is a boolean
        if pay is not None:
            result = result.filter(paid=pay)

        # parameter type is an array of strings
        if tp is not None:
            result = result.filter(type__in=type)

        # perform keyword search
        if isinstance(keywords, (list,)):
            if len(keywords) == 0:
                threshold = INFINITY
            else:
                threshold = ceil(RELEVANT_COEFFICIENT * len(keywords))

            for job in result:
                # description pre-processing
                full_description = job.job_position + ' ' + job.company.company_name
                full_description = string_preprocess(full_description)

                # comparing keywords with job descriptions
                matched = 0
                for word in keywords:
                    if word in full_description:
                        matched += 1

                result = set(result)
                if matched < threshold:
                    result.discard(job)

        return list(result)

        # # job type parameter
        # if type is not None:
        #     for job in list(result):
        #         for job_type in type:
        #             if job.type != job_type:
        #                 result.remove(job)

        # # degree parameter is a string
        # if degs is not None:
        #     relevant_Jobs = []
        #     for job in result:
        #         for deg in degs:
        #             if deg in [dg.degree for dg in job.Degree_Require.all()]:
        #                 relevant_Jobs.append(job)
        #     result = relevant_Jobs

        # # start_date parameter is a number
        # if start_date is not None:
        #     relevant_Jobs = []
        #     for job in result:
        #         if job.job_start == start_date:
        #             relevant_Jobs.append(job)
        #     result = relevant_Jobs

        # # start_date parameter is a number
        # if end_date is not None:
        #     relevant_Jobs = []
        #     for job in result:
        #         if job.job_end == end_date:
        #             relevant_Jobs.append(job)
        #     result = relevant_Jobs

        # # location parameter is a string
        # if location is not None:
        #     relevant_Jobs = []
        #     location = location.lower()
        #     for job in result:
        #         if location in job.job_location:
        #             relevant_Jobs.append(job)
        #     result = relevant_Jobs

        # # paid parameter is a boolean
        #         # if pay is not None:
        #         #     relevant_Jobs = []
        #         #     for job in result:
        #         #         if job.job_paid == pay:
        #         #             relevant_Jobs.append(job)
        #         #     result = relevant_Jobs


    @staticmethod
    def get_all():
        return list(Job.objects.all())

    @staticmethod
    def search_By_Keywords(keywords):
        if type(keywords) != str:
            return False
        else:
            # keywords pre-processing:
            keywords = string_preprocess(keywords)

            relavent_Jobs = []
            threshold = ceil(RELEVANT_COEFFICIENT * len(keywords))
            for job in Job.objects.all():
                # description pre-processing
                full_description = job.description + ' ' + job.job_position + ' ' + job.company.company_name
                full_descroption = string_preprocess(full_description)

                # comparing keywords with job descriptions
                counter = 0
                for word in keywords:
                    if word in full_descroption:
                        counter += 1

                if counter >= threshold:
                    relavent_Jobs.append(job)
            return relavent_Jobs

    @staticmethod
    def get_Job_Company(company):
        if type(company) != Company.models.Company:
            return False
        else:
            return Job.objects.filter(Company=company)

    # get_Job_Work_Auth

    @staticmethod
    def get_Job_Work_Auth(work_auth):
        if type(work_auth) != str:
            return False
        else:
            return Job.objects.filter(WorkAuthorization=work_auth)

    # get_Job_Position

    @staticmethod
    def get_Job_Position(position):
        if type(position) != str:
            return False
        else:
            return Job.objects.filter(job_position=position)


    # get_Job_URL

    @staticmethod
    def get_Job_URL(url):
        if type(url) != str:
            return False
        else:
            return Job.objects.filter(job_URL=url)

    # get_Job_Major_Require

    @staticmethod
    def get_Job_Major_Require(major):
        if type(major) != Major:
            return False
        else:
            return Job.objects.filter(Major_Require=major)


    # get_Job_Degree_Require

    @staticmethod
    def get_Job_Degree_Require(degree):
        if type(degree) != Degree:
            return False
        else:
            return Job.objects.filter(Degree_Require=degree)


    # get_Job_Duration

    @staticmethod
    def get_Job_Duration(duration):
        if type(duration) != str:
            return False
        else:
            return Job.objects.filter(job_duration=duration)

    # get_Job_location

    @staticmethod
    def get_Job_location(location):
        if type(location) != str:
            return False
        else:
            return Job.objects.filter(job_location=location)


    # get_Job_paid

    @staticmethod
    def get_Job_paid(paid):
        if type(paid) != bool:
            return False
        else:
            return Job.objects.filter(job_paid=paid)


    # setter

    # set_Job_Position

    def set_Job_Position(self, position):
        if type(position) != str:
            return False
        else:
            self.job_position = position
            return True

    # set_Job_Company

    def set_Job_Company(self, company):
        if type(company) != Company.models.Company:
            return False
        else:
            self.company = company
            return True


    # set_Job_Duration


    def set_Job_Duration(self, duration):
        if type(duration) != str:
            return False
        else:
            self.job_duration = duration
            return True


    # set_Job_Major_Require


    def set_major(self, major):
        if type(major) != Major:
            return False
        else:
            self.Major_Require = major
            return True


    # set_Job_Degree_Require


    def set_degree(self, degree):
        if type(degree) != Degree:
            return False
        else:
            self.Degree_Require = degree
            return True


    # set_Job_Work_Auth


    def set_Job_Work_Auth(self, work_auth):
        if type(work_auth) != str:
            return False
        else:
            self.job_Work_Auth = work_auth
            return True


    # set_Job_paid

    def set_Job_paid(self, paid):
        if type(paid) != bool:
            return False
        else:
            self.job_paid = paid
            return True

    def update_num_favorite(self):
        self.num_favorites = self.favorited_user.all().count()
        return

    def increment_num_views(self):
        self.num_views += 1
        return

    # add_to_favorite
    def add_to_favorite(self, user):
        if type(user) != User:
            return False
        else:
            if self.favorited_user.filter(id=user.id):
                self.favorited_user.remove(user)
            else:
                self.favorited_user.add(user)
        self.update_num_favorite()
        return True

    # get_favorite_status
    def get_favorite_status(self, user):
        if type(user) != User:
            return False
        else:
            if self.favorited_user.filter(id=user.id):
                return True
            else:
                return False


# class Referral(models.Model):
#     referral_ID = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
#     ref_provider = models.ForeignKey(User, on_delete=models.PROTECT)
#     referral_job = models.ForeignKey(Job, on_delete=models.PROTECT)
#     referral_description = models.CharField(max_length=300)
#     resume_require = models.BooleanField
#
#
# # getter
#
#
# # get_provider
#
#
# def get_provider(provider):
#     if type(provider) != User:
#         return False
#     else:
#         return Referral.objects.all.filter(ref_provider=provider)
#
#
# # setter
#
# def set_resume_require(self, res_require):
#     if type(res_require) != bool:
#         return False
#     else:
#         self.resume_require = res_require
#         return True
