import uuid
from datetime import datetime

import django.core.validators
from django.db import models

import Company.models
from User.models import Major, Degree, User
import string
from math import ceil
from nltk.corpus import stopwords
from nltk.stem.porter import *
from django.utils import timezone


##################################### Constants

WORKAUTHS=(
    ('U.S. Citizens','U.S. Citizens Or U.S. Permanent Residents Only'),
    ('Other','All Legal Citizens'),
)

JOBTYPES=(
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
RELEVANT_COEFFICIENT = 0.5
INFINITY = 999999


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
    post_time = models.DateTimeField(default=datetime.now, blank=True)

    # from data
    job_position = models.CharField(max_length=200)
    type = models.CharField(max_length=100, choices=JOBTYPES)
    description = models.CharField(max_length=100000)
    job_Work_Auth = models.CharField(max_length=100, choices=WORKAUTHS)
    company = models.ForeignKey(Company.models.Company, on_delete=models.PROTECT)
    job_URL = models.URLField(max_length=300)
    degree_required = models.ManyToManyField(Degree, null=True, blank=True)
    major_required = models.ManyToManyField(Major, null=True, blank=True)


    @staticmethod
    def general_Search(keywords, work_auth, degs, start_date, end_date, location, pay, type):
        result = [job for job in Job.objects.all()]

        #     def _perform keyword search if keyword is not none
        if keywords is not None:
            # keywords pre-processing:
            keywords = string_preprocess(keywords)

            relevant_Jobs = []
            if len(keywords) == 0:
                threshold = INFINITY
            else:
                threshold = ceil(RELEVANT_COEFFICIENT * len(keywords))
            for job in result:
                # description pre-processing
                full_description = job.description + ' ' + job.job_position + ' ' + job.company.company_name
                full_description = string_preprocess(full_description)

                # comparing keywords with job descriptions
                counter = 0
                for word in keywords:
                    if word in full_description:
                        counter += 1

                if counter >= threshold:
                    relevant_Jobs.append(job)
            result = relevant_Jobs

        # work authorization parameter is a string
        if work_auth is not None:
            relevant_Jobs = []
            for job in result:
                for auth in work_auth:
                    if job.job_Work_Auth == auth:
                        relevant_Jobs.append(job)
            result = relevant_Jobs

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

        return result


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
