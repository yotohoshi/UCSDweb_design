from django.db import models


# Create your models here.


class Company(models.Model):
    db_table = 'Company',
    company_name = models.CharField(max_length=100, primary_key=True, unique=True)
    description = models.CharField(max_length=300, default="This company have no descriptions yet.")

    # category = ...

    # Getters
    # get_Company_Name() TODO

    @staticmethod
    def getCompanyList():
        return [dic['company_name'] for dic in Company.objects.values('company_name')]

# get_Description() TODO
