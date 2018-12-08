from User.models import Major, Degree, User
from Company.models import Company
from Event.models import Event
from Job.models import Job, Location
from Category.models import Category
import json

#####################################################################
print('reading json data')
with open('Users Data.json') as file:
    data = json.load(file)

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

#########################################################################
print('creating company objects')

companies = set()
for user in data:
    if user['company'] is not None:
        companies.add(user['company'].lower())

companies = list(companies)
for company in companies:
    Company.objects.create(company_name=company, description="Not Available Now")

#########################################################################
print('creating user objects')

i = 1
for user in data:
    print('creating user ' + str(i))
    curUser = User.objects.create(
        F_Name=user['F_Name'],
        L_Name=user['L_Name'],
        yr_graduation=user['yr_graduation'],
        major=Major.objects.get(major=user['major']),
        degree=Degree.objects.get(degree=user['degree']),
        contact_email=user['contact_email'],
        description=user['description'],
        referral_ability=user['referral_ability'],
    )

    if user['company'] is not None:
        curUser.company = Company.objects.get(company_name=(user['company'].lower()))

    for friendEmail in user['friend']:
        curUser.friend.add(User.objects.get(contact_email=friendEmail))

    i += 1
    curUser.save()
