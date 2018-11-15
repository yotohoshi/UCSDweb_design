from django.db import models
import uuid
import User.models
import Job.models
import django.core.validators


# Create your models here.


class Referral(models.Model):
    referral_ID = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    ref_provider = models.ForeignKey(User.models.User, on_delete=models.PROTECT)
    referral_job = models.ForeignKey(Job.models.Job, on_delete=models.PROTECT)
    referral_description = models.CharField(max_length=300)
    resume_require = models.BooleanField


# getter


# get_provider


def get_provider(provider):
    if type(provider) != User.models.User:
        return False
    else:
        return Referral.objects.all.filter(ref_provider=provider)


# setter

def set_resume_require(self, res_require):
    if type(res_require) != bool:
        return False
    else:
        self.resume_require = res_require
        return True
