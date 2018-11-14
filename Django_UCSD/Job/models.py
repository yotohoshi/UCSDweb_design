from django.db import models
import uuid
import django.core.validators
import Company.models
import User.models

# Create your models here.


class WorkAuthorization(models.Model):
    db_table = 'WorkAuthorization'
    Work_Auth = models.CharField(max_length=100)


class Job(models.Model):
    db_table = 'Job'
    JobID = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    job_position = models.CharField(max_length=200)
    type = models.IntegerField(validators=[django.core.validators.MaxValueValidator(1, message=None),django.core.validators.MinValueValidator(0, message=None)])
    description = models.CharField(max_length=300)
    company = models.ForeignKey(Company, on_delete=models.PROTECT)
    job_URL = models.URLField(max_length=300)
    job_duration = models.CharField(max_length=100)
    job_location = models.CharField(max_length=100)
    job_Work_Auth = models.ForeignKey(WorkAuthorization, on_delete=models.PROTECT)
    job_paid = models.BooleanField
    Major_Require = models.ManyToManyField(User.models.Major, symmetrical=False, blank=True)
    Degree_Require = models.ManyToManyField(User.models.Degree, symmetrical=False, blank=True)


    # getter

    # get_Job_Company


    def get_Job_Company(company):
        if type(company) != Company.models.Company:
            return False
        else:
            return Job.objects.all.filter(Company=company)

    # get_Job_Work_Auth


    def get_Job_Work_Auth(work_auth):
        if type(work_auth) != WorkAuthorization:
            return False
        else:
            return Job.objects.all.filter(WorkAuthorization=work_auth)

    # get_Job_Position


    def get_Job_Position(position):
        if type(position) != str:
            return False
        else:
            return Job.objects.all.filter(job_position=position)


    # get_Job_URL


    def get_Job_URL(url):
        if type(url) != str:
            return False
        else:
            return Job.objects.all.filter(job_URL=url)

    # get_Job_Major_Require


    def get_Job_Major_Require(major):
        if type(major) != User.models.Major:
            return False
        else:
            return Job.objects.all.filter(Major_Require=major)


    # get_Job_Degree_Require


    def get_Job_Degree_Require(degree):
        if type(degree) != User.models.Degree:
            return False
        else:
            return Job.objects.all.filter(Degree_Require=degree)


    # get_Job_Duration


    def get_Job_Duration(duration):
        if type(duration) != str:
            return False
        else:
            return Job.object.all.filter(job_duration=duration)

    # get_Job_location


    def get_Job_location(location):
        if type(location) != str:
            return False
        else:
            return Job.object.all.filter(job_location=location)


    # get_Job_paid


    def get_Job_paid(paid):
        if type(paid) != bool:
            return False
        else:
            return Job.object.all.filter(job_paid=paid)


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
        if type(work_auth) != WorkAuthorization:
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