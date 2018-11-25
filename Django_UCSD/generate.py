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

################################################################3
print('creating major objects')
major1 = Major.objects.create(major="ECE")
major1.save()

##########################################################################
print('creating degree objects')
degree1 = Degree.objects.create(degree="BS")
degree1.save()

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
event1=Event.objects.create(
    event_name="1Apple_workshop",
    date = "2018-12-20",
    time = "10:00",
    company = company2,
    location = "ucsd",
    type = 0,
    description = "help people learn coding",
    num_views = 12032,
    num_favorites=8473)
event1.save()

###################################################################
print('creating job objects')

for job in data:
    curJob=Job.objects.create(job_position = job['position'],
        type = job['type'],
        description = job['description'],
        job_Work_Auth = job['authorization'],
        company = Company.objects.get(company_name=job['company']),
        job_URL = job['url'],
        #job_location = job['location'],
        )
    curJob.save()