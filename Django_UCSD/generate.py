#python3 manage.py flush
#yes
#python3 manage.py createsuperuser
#
#python3 manage.py shell < generate.py
#python3 manage.py runserver

from User.models import Major, Degree, User
from Company.models import Company
from Event.models import Event
#print("start")
major1 = Major.objects.create(major="ECE")
major1.save()
major2 = Major.objects.create(major="EE")
major2.save()
major3 = Major.objects.create(major="CS")
major3.save()
major4 = Major.objects.create(major="MATH")
major4.save()
major5 = Major.objects.create(major="ENVIRONMENT")
major5.save()
major6 = Major.objects.create(major="BUSINESS")
major6.save()
major7 = Major.objects.create(major="CE")
major7.save()
major8 = Major.objects.create(major="ENGLISH")
major8.save()
major9 = Major.objects.create(major="CHINESE")
major9.save()
major10 = Major.objects.create(major="SEX")
major10.save()

degree1 = Degree.objects.create(degree="BS")
degree1.save()
degree2 = Degree.objects.create(degree="PHD")
degree2.save()
degree3 = Degree.objects.create(degree="MS")
degree3.save()
degree4 = Degree.objects.create(degree="SEXY")
degree4.save()

company1 =Company.objects.create(company_name="Google")
company2 =Company.objects.create(company_name="Apple",description="very fashionable")
company3 =Company.objects.create(company_name="Pornhub",description="sexy, daluo likes it")
company4 =Company.objects.create(company_name="Facebook",description="make friend")
company5 =Company.objects.create(company_name="Amazon",description="buy product")
company6 =Company.objects.create(company_name="LinkedIn",description="qwer")
company7 =Company.objects.create(company_name="Sensetime",description="research")
company8 =Company.objects.create(company_name="Microsoft",description="tech")
company9 =Company.objects.create(company_name="Airbnb",description="baby")
company10 =Company.objects.create(company_name="doodle",description="..")
company11 =Company.objects.create(company_name="dudu",description=".")

user1 = User.objects.create(F_Name="ShihHan", L_Name="Chan", yr_graduation=2040, major=major4, degree=degree3,
                                    contact_email="hank08tw@gmail.com",
                                    description="bigdickman.vpwieljrnpvqoiunvpwoieurvqoie;urbv;lefkbv;osldkfjbs;lkdfjbv;sldkfjhbsldfjhv s;adlkfhjb;alkdsfjbv;aslkdfjv;lkdfjv;aA;SLDKFJA;SLDKFJA;SLDKFJA;LSDKFJ;ALSDKFJA;SLDKFJA;SLKDFJkdsfjnv",
                                    register_email="hank08tw@gmail.com", password="1234qwerasdfzxcv")
user1.save()

user2 = User.objects.create(F_Name="ren", L_Name="Ga", yr_graduation=2030, major=major5, degree=degree4,
                                    contact_email="garenopop@gmail.com",
                                    description="asdfjnvpwieljrnpasdfklj;lkjasdfoieurvqoie;urbv;lefkbv;osldkfjbs;lkdfjbv;sldkfjhbsldfjhv s;adlkfhjb;alkdsfjbv;aslkdfjv;lkdfjv;aA;SLDKFJA;SLDKFJA;SLDKFJA;LSDKFJ;ALSDKFJA;SLDKFJA;SLKDFJkdsfjnv",
                                    register_email="garenopop123@gmail.com", password="noseemypasswordok")
user2.save()


user3 = User.objects.create(F_Name="GAGA", L_Name="LADY", yr_graduation=2020, major=major10, degree=degree3,
                                    contact_email="gogogolady123@gmail.com",
                                    description="Someone wants to have sex with every girl. Hint: He likes to go pub and ooxx. oiunvpwoieurvqoie;urbv;lefkbv;osldkfjbs;lkdfjbv;sldkfjhbsldfjhv s;adlkfhjb;alkdsfjbv;aslkdfjv;lkdfjv;aA;SLDKFJA;SLDKFJA;SLDKFJA;LSDKFJ;ALSDKFJA;SLDKFJA;SLKDFJkdsfjnv",
                                    register_email="ladytitbig123@gmail.com", password="1234qwerasdfzxcv")
user3.save()
user4 = User.objects.create(F_Name="SUCK", L_Name="LUX", yr_graduation=2021, major=major7, degree=degree4,
                                    contact_email="whatisthatballd@gmail.com",
                                    description="a;sldkfjas;lkdfjnvpwieljrnpvqoiunvpwoieurvqoie;urbv;lefkbv;osldkfjbs;lkdfjbv;sldkfjhbsldfjhv s;adlkfhjb;alkdsfjbv;aslkdfjv;lkdfjv;aA;SLDKFJA;SLDKFJA;SLDKFJA;LSDKFJ;ALSDKFJA;SLDKFJA;SLKDFJkdsfjnv",
                                    register_email="whatsupsucksuck1@gmail.com", password="1234qwerasdfzxcv")
user4.save()
user5 = User.objects.create(F_Name="you", L_Name="fvck", yr_graduation=2040, major=major4, degree=degree3,
                                    contact_email="ABCDEFG23333@gmail.com",
                                    description="SUck my dick mother fucker!!!jnvpwieljrnpvqoiunvpwoieurvqoie;urbv;lefkbv;osldkfjbs;lkdfjbv;sldkfjhbsldfjhv s;adlkfhjb;alkdsfjbv;aslkdfjv;lkdfjv;aA;SLDKFJA;SLDKFJA;SLDKFJA;LSDKFJ;ALSDKFJA;SLDKFJA;SLKDFJkdsfjnv",
                                    register_email="fvckmesohardbaby@gmail.com", password="1234qwerasdfzxcv")
user5.save()
user6 = User.objects.create(F_Name="stupid", L_Name="Gary", yr_graduation=2049, major=major3, degree=degree3,
                                    contact_email="Garysolame@ucsd.edu",
                                    description="dalou cool.npvqoiunvpwoieurvqoie;urbv;lefkbv;osldkfjbs;lkdfjbv;sldkfjhbsldfjhv s;adlkfhjb;alkdsfjbv;aslkdfjv;lkdfjv;aA;SLDKFJA;SLDKFJA;SLDKFJA;LSDKFJ;ALSDKFJA;SLDKFJA;SLKDFJkdsfjnv",
                                    register_email="garyisreallystupid@gmail.com", password="1234qwerasdfzxcv")
user6.save()
user7 = User.objects.create(F_Name="jobs", L_Name="steve", yr_graduation=2019, major=major8, degree=degree4,
                                    contact_email="stevedadada@apple.com",
                                    description="a;sldkfjas;lkdfjnvpwieljrnpvqoiunvpwoieurvqoie;urbv;lefkbv;osldkfjbs;lkdfjbv;sldkfjhbsldfjhv s;adlkfhjb;alkdsfjbv;aslkdfjv;lkdfjv;aA;SLDKFJA;SLDKFJA;SLDKFJA;LSDKFJ;ALSDKFJA;SLDKFJA;SLKDFJkdsfjnv",
                                    register_email="stevesteve@gmail.com", password="12345qwer")
user7.save()
user8 = User.objects.create(F_Name="Atrox", L_Name="Akali", yr_graduation=2039, major=major6, degree=degree3,
                                    contact_email="Akalisuckatrox@gmail.com",
                                    description="i like titttttttttttttttyjas;lkdfjnvpwieljrnpvqoiunvpwoieurvqoie;urbv;lefkbv;osldkfjbs;lkdfjbv;sldkfjhbsldfjhv s;adlkfhjb;alkdsfjbv;aslkdfjv;lkdfjv;aA;SLDKFJA;SLDKFJA;SLDKFJA;LSDKFJ;ALSDKFJA;SLDKFJA;SLKDFJkdsfjnv",
                                    register_email="23cmadmiremehaha@gmail.com", password="23cm23cm23cm23cm")
user8.save()
user9 = User.objects.create(F_Name="harry", L_Name="jeff", yr_graduation=2021, major=major9, degree=degree4,
                                    contact_email="jeffrey@gmail.com",
                                    description="hohohohohohos;lkdfjnvpwieljrnpvqoiunvpwoieurvqoie;urbv;lefkbv;osldkfjbs;lkdfjbv;sldkfjhbsldfjhv s;adlkfhjb;alkdsfjbv;aslkdfjv;lkdfjv;aA;SLDKFJA;SLDKFJA;SLDKFJA;LSDKFJ;ALSDKFJA;SLDKFJA;SLKDFJkdsfjnv",
                                    register_email="jeffistall123@gmail.com", password="1234qwerasdfzxcv")
user9.save()
user10 = User.objects.create(F_Name="Board", L_Name="Key", yr_graduation=2019, major=major6, degree=degree4,
                                    contact_email="slushpeoplekingz@gmail.com",
                                    description="keyboard likes to eat shit.;lkdfjnvpwieljrnpvqoiunvpwoieurvqoie;urbv;lefkbv;osldkfjbs;lkdfjbv;sldkfjhbsldfjhv s;adlkfhjb;alkdsfjbv;aslkdfjv;lkdfjv;aA;SLDKFJA;SLDKFJA;SLDKFJA;LSDKFJ;ALSDKFJA;SLDKFJA;SLKDFJkdsfjnv",
                                    register_email="ohohhohohohododo@gmail.com", password="nastybiches6969")
user10.save()



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

event2=Event.objects.create(
    event_name="2google_workshop",
    date = "2018-11-14",
    time = "12:30",
    company = company1,
    location = "mountainview",
    type = 1,
    description = "google intern possibilities",
    num_views = 8594,
    num_favorites=3897)

event3=Event.objects.create(
    event_name="3amazon_party",
    date = "2019-1-13",
    time = "23:00",
    company = company5,
    location = "CA,LA",
    type = 0,
    description = "drink and know friends from amazon",
    num_views = 6578,
    num_favorites=2567)

event4=Event.objects.create(
    event_name="4Sensetime_talk",
    date = "2018-12-23",
    time = "9:00",
    company = company7,
    location = "UTC",
    type = 1,
    description = "learn how to do research",
    num_views = 6498,
    num_favorites=2390)

event5=Event.objects.create(
    event_name="5Microsoft_codejam",
    date = "2018-11-28",
    time = "14:00",
    company = company8,
    location = "ucsd",
    type = 0,
    description = "interesting coding contest",
    num_views = 5896,
    num_favorites=1893)

event6=Event.objects.create(
    event_name="linkedIn_workshop",
    date = "2018-12-12",
    time = "16:00",
    company = company6,
    location = "pc",
    type = 0,
    description = "help people learn about the company",
    num_views = 3478,
    num_favorites=1453)

event7=Event.objects.create(
    event_name="doodle_workshop",
    date = "2018-11-28",
    time = "17:00",
    company = company10,
    location = "forest",
    type = 1,
    description = "help people learn coding",
    num_views = 2367,
    num_favorites=1321)

event8=Event.objects.create(
    event_name="Pornhub_watchvideo",
    date = "2018-11-25",
    time = "21:00",
    company = company4,
    location = "home",
    type = 1,
    description = "watch some special video",
    num_views = 1567,
    num_favorites=1023)

event9=Event.objects.create(
    event_name="Airbnb_workshop",
    date = "2019-1-16",
    time = "10:30",
    company = company10,
    location = "japan",
    type = 1,
    description = "make love",
    num_views = 894,
    num_favorites=578)

event10=Event.objects.create(
    event_name="dudu_workshop",
    date = "2019-2-11",
    time = "14:30",
    company = company11,
    location = "Taiwan",
    type = 1,
    description = "dududududodododo",
    num_views = 322,
    num_favorites=133)