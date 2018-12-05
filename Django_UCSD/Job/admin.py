from django.contrib import admin
from Job.models import Job, Location, Referral


# Register your models here.


admin.site.register(Job)
admin.site.register(Location)
admin.site.register(Referral)

