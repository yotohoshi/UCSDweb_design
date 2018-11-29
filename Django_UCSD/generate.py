#python3 manage.py flush
#yes
#python3 manage.py createsuperuser
#
#python3 manage.py shell < generate.py
#python3 manage.py runserver

from User.models import Major, Degree, User
from Company.models import Company
from Event.models import Event
from Job.models import Job
import json

##########################################################################
# print('creating degree objects')
# degree1 = Degree.objects.create(degree="BS")
# degree1.save()

##########################################################################
print('creating degree objects')
degree1 = Degree.objects.create(degree="BS")
degree1.save()
degree2 = Degree.objects.create(degree="PHD")
degree2.save()
degree3 = Degree.objects.create(degree="MS")
degree3.save()
degree4 = Degree.objects.create(degree="BA")
degree4.save()
degree5 = Degree.objects.create(degree="MBA")
degree5.save()
degree6 = Degree.objects.create(degree="NOT REQUIRED")
degree6.save()

################################################################3
print('creating major objects')
major1 = Major.objects.create(major="NOT LISTED")
major1.save()
major2 = Major.objects.create(major="ELECTRIC ENGINEERING")
major2.save()
major3 = Major.objects.create(major="COMPUTER SCIENCE")
major3.save()
major4 = Major.objects.create(major="MATH")
major4.save()
major5 = Major.objects.create(major="ENVIRONMENT")
major5.save()
major6 = Major.objects.create(major="BUSINESS")
major6.save()
major7 = Major.objects.create(major="COMPUTER ENGINEERING")
major7.save()
major8 = Major.objects.create(major="ENGLISH")
major8.save()
major9 = Major.objects.create(major="CHINESE")
major9.save()
major10 = Major.objects.create(major="ARCHITECTURE")
major10.save()
major11 = Major.objects.create(major="ANTHROPOLOGY")
major11.save()
major12 = Major.objects.create(major="ARCHAEOLOGY")
major12.save()
major13 = Major.objects.create(major="BIOLOGY")
major13.save()
major14 = Major.objects.create(major="BIOENGINEERING")
major14.save()
major15 = Major.objects.create(major="CHEMISTRY")
major15.save()
major16 = Major.objects.create(major="CIVIL AND ENVIRONMENTAL ENGINEERING")
major16.save()
major17 = Major.objects.create(major="ART")
major17.save()
major18 = Major.objects.create(major="PHILOSOPHY")
major18.save()
major19 = Major.objects.create(major="HISTORY")
major19.save()
major20 = Major.objects.create(major="DATA SCIENCE")
major20.save()
major21 = Major.objects.create(major="STATISTICS")
major21.save()
major23 = Major.objects.create(major="ELECTRONIC SPORTS")
major23.save()
major24 = Major.objects.create(major="COMMUNICATION")
major24.save()
major24 = Major.objects.create(major="ECONOMICS")
major24.save()
#########################################################################
print('creating company objects')
with open('Jobs Data.json') as file:
    data = json.load(file)

companies = set()
for job in data:
    companies.add(job['company'].lower())

companies = list(companies)
for company in companies:
    Company.objects.create(company_name=company, description="Not Available Now")

#########################################################################
print('creating event objects')
# event1=Event.objects.create(
#     event_name="1Apple_workshop",
#     date = "2018-12-20",
#     time = "10:00",
#     company = company2,
#     location = "ucsd",
#     type = 0,
#     description = "help people learn coding",
#     num_views = 12032,
#     num_favorites=8473)
# event1.save()

###################################################################
print('creating job objects')

for job in data:
    curJob = Job.objects.create(job_position=job['position'],
                                type=job['type'],
                                description=job['description'],
                                short_description=job['summary'],
                                job_Work_Auth=job['authorization'],
                                company=Company.objects.get(company_name=(job['company'].lower())),
                                job_URL=job['url']
                                # job_location = job['location'],
                                )
    for majorName in job['major']:
        curJob.major_required.add(Major.objects.get(major=majorName))
    curJob.degree_required.add(Degree.objects.get(degree=job['degree']))
    curJob.save()
