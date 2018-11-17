import uuid

import django.core.validators
from django.db import models

import Company.models
import User.models
import string
from math import ceil
from nltk.corpus import stopwords
from nltk.stem.porter import *


##################################### Constants

WORKAUTHS=(
    ('U.S Citizen','U.S Citizen'),
    ('Permanent Resident','Permanent Resident'),
    ('F-1','F-1'),
    ('H1-B','H1-B'),
    ('Otherwise','Otherwise Authorized to Work'),
)
PUNCTUATIONS = set(string.punctuation)
STOPWORDS = set(stopwords.words('english'))
STEMMER = PorterStemmer()
RELEVANT_COEFFICIENT = 0.5


##################################### Helper Methods
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


#################################### Models

class Job(models.Model):
    db_table = 'Job'
    JobID = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    entry_creation = models.DateTimeField(auto_now_add=True)
    job_position = models.CharField(max_length=200)
    type = models.IntegerField(validators=[django.core.validators.MaxValueValidator(1, message=None),
                                           django.core.validators.MinValueValidator(0, message=None)])
    description = models.CharField(max_length=300)
    company = models.ForeignKey(Company.models.Company, on_delete=models.PROTECT)
    job_URL = models.URLField(max_length=300)
    job_duration = models.CharField(max_length=100)
    #job_start = models.DateTimeField()
    #job_end = models.DateTimeField()
    job_location = models.CharField(max_length=100)
    job_Work_Auth = models.CharField(max_length = 100, choices = WORKAUTHS)
    job_paid = models.BooleanField
    Major_Require = models.ManyToManyField(User.models.Major, symmetrical=False, blank=True)
    Degree_Require = models.ManyToManyField(User.models.Degree, symmetrical=False, blank=True)



    # string representation of Job instances
    def __str__(self):
        return str(self.entry_creation)

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
        if type(major) != User.models.Major:
            return False
        else:
            return Job.objects.filter(Major_Require=major)


    # get_Job_Degree_Require

    @staticmethod
    def get_Job_Degree_Require(degree):
        if type(degree) != User.models.Degree:
            return False
        else:
            return Job.objects.filter(Degree_Require=degree)


    # get_Job_Duration

    @staticmethod
    def get_Job_Duration(duration):
        if type(duration) != str:
            return False
        else:
            return Job.object.filter(job_duration=duration)

    # get_Job_location

    @staticmethod
    def get_Job_location(location):
        if type(location) != str:
            return False
        else:
            return Job.object.filter(job_location=location)


    # get_Job_paid

    @staticmethod
    def get_Job_paid(paid):
        if type(paid) != bool:
            return False
        else:
            return Job.object.filter(job_paid=paid)


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
        if type(major) != User.models.Major:
            return False
        else:
            self.Major_Require = major
            return True


    # set_Job_Degree_Require


    def set_degree(self, degree):
        if type(degree) != User.models.Degree:
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