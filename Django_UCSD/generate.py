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

################################################################3
# print('creating major objects')
# major1 = Major.objects.create(major="ECE")
# major1.save()

##########################################################################
# print('creating degree objects')
# degree1 = Degree.objects.create(degree="BS")
# degree1.save()

#########################################################################
print('creating company objects')
with open('Jobs_Data.json') as file:
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
                                job_Work_Auth=job['authorization'],
                                company=Company.objects.get(company_name=(job['company'].lower())),
                                job_URL=job['url']
                                # job_location = job['location'],
                                )

curJob.save()


from User.models import Major, Degree, User
from Company.models import Company
from Event.models import Event
from Job.models import Job
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
major21 = Major.objects.create(major="STATISTIC")
major21.save()
major22 = Major.objects.create(major="NO LIMITED")
major22.save()
major23 = Major.objects.create(major="ELECTRONIC SPORTS")
major23.save()
major24 = Major.objects.create(major="COMMUNICATION")
major24.save()


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
degree6 = Degree.objects.create(degree="NO LIMITED")
degree6.save()


company1 =Company.objects.create(company_name="Google",description="Google LLC[5] is an American multinational technology company that specializes in Internet-related services and products, which include online advertising technologies, search engine, cloud computing, software, and hardware. Google was founded in 1998 by Larry Page and Sergey Brin while they were Ph.D. students at Stanford University in California. Together they own about 14 percent of its shares and control 56 percent of the stockholder voting power through supervoting stock. They incorporated Google as a privately held company on September 4, 1998. An initial public offering (IPO) took place on August 19, 2004, and Google moved to its headquarters in Mountain View, California, nicknamed the Googleplex. In August 2015, Google announced plans to reorganize its various interests as a conglomerate called Alphabet Inc. Google is Alphabet's leading subsidiary and will continue to be the umbrella company for Alphabet's Internet interests. Sundar Pichai was appointed CEO of Google, replacing Larry Page who became the CEO of Alphabet.")
company1.save()
company2 =Company.objects.create(company_name="Apple",description="Apple Inc. is an American multinational technology company headquartered in Cupertino, California, that designs, develops, and sells consumer electronics, computer software, and online services. The company's hardware products include the iPhone smartphone, the iPad tablet computer, the Mac personal computer, the iPod portable media player, the Apple Watch smartwatch, the Apple TV digital media player, and the HomePod smart speaker. Apple's software includes the macOS and iOS operating systems, the iTunes media player, the Safari web browser, and the iLife and iWork creativity and productivity suites, as well as professional applications like Final Cut Pro, Logic Pro, and Xcode. Its online services include the iTunes Store, the iOS App Store and Mac App Store, Apple Music, and iCloud.")
company2.save()
company3 =Company.objects.create(company_name="Pornhub",description="Everyone likes it!")
company3.save()
company4 =Company.objects.create(company_name="Facebook",description="Facebook, Inc. is an American online social media and social networking service company based in Menlo Park, California. Its website was launched on February 4, 2004, by Mark Zuckerberg, along with fellow Harvard College students and roommates Eduardo Saverin, Andrew McCollum, Dustin Moskovitz and Chris Hughes.")
company4.save()
company5 =Company.objects.create(company_name="Amazon",description="Amazon.com, Inc., doing business as Amazon, is an American electronic commerce and cloud computing company based in Seattle, Washington, that was founded by Jeff Bezos on July 5, 1994. The tech giant is the largest Internet retailer in the world as measured by revenue and market capitalization, and second largest after Alibaba Group in terms of total sales.[5] The Amazon.com website started as an online bookstore and later diversified to sell video downloads/streaming, MP3 downloads/streaming, audiobook downloads/streaming, software, video games, electronics, apparel, furniture, food, toys, and jewelry. The company also owns a publishing arm, Amazon Publishing, a film and television studio, Amazon Studios, produces consumer electronics lines including Kindle e-readers, Fire tablets, Fire TV, and Echo devices, and is the world's largest provider of cloud infrastructure services (IaaS and PaaS) through its AWS subsidiary.[6] Amazon also sells certain low-end products under its in-house brand AmazonBasics.")
company5.save()
company6 =Company.objects.create(company_name="LinkedIn",description="LinkedIn is a business and employment-oriented service that operates via websites and mobile apps. Founded on December 28, 2002,[4] and launched on May 5, 2003,[5] it is mainly used for professional networking, including employers posting jobs and job seekers posting their CVs. As of 2015, most of the company's revenue came from selling access to information about its members to recruiters and sales professionals.[6] As of October 2018, LinkedIn had 590 million registered members in 200 countries, out of which more than 250 million active users.[3] LinkedIn allows members (both workers and employers) to create profiles and connections to each other in an online social network which may represent real-world professional relationships. Members can invite anyone (whether an existing member or not) to become a connection.[7] The gated-access approach (where contact with any professional requires either an existing relationship or an introduction through a contact of theirs) is intended to build trust among the service's members. LinkedIn participated in the EU's International Safe Harbor Privacy Principles.[8]")
company6.save()
company7 =Company.objects.create(company_name="Sensetime",description="SenseTime is a Chinese technology company specializing in artificial intelligence and facial recognition, with offices across China, Hong Kong and Japan. Its products serve over hundreds of well-known companies and government agencies, across a wide range of industries including security, finance, smartphones, mobile Internet, robotics, and automobile.")
company7.save()
company8 =Company.objects.create(company_name="Microsoft",description="Microsoft Corporation (MS) is an American multinational technology company with headquarters in Redmond, Washington. It develops, manufactures, licenses, supports and sells computer software, consumer electronics, personal computers, and related services. Its best known software products are the Microsoft Windows line of operating systems, the Microsoft Office suite, and the Internet Explorer and Edge web browsers. Its flagship hardware products are the Xbox video game consoles and the Microsoft Surface lineup of touchscreen personal computers. As of 2016, it is the world's largest software maker by revenue, and one of the world's most valuable companies. The word Microsoft is a portmanteau of microcomputer and software.[5] Microsoft is ranked No. 30 in the 2018 Fortune 500 rankings of the largest United States corporations by total revenue.")
company8.save()
company9 =Company.objects.create(company_name="Airbnb",description="Airbnb is a privately held global company headquartered in San Francisco that operates an online marketplace and hospitality service which is accessible via its websites and mobile apps. Members can use the service to arrange or offer lodging, primarily homestays, or tourism experiences. The company does not own any of the real estate listings, nor does it host events; as a broker, it receives commissions from every booking.[3]")
company9.save()
company10 =Company.objects.create(company_name="Baidu",description="Baidu, Inc. incorporated on 18 January 2000, is a Chinese multinational technology company specializing in Internet-related services and products and artificial intelligence, headquartered at the Baidu Campus in Beijing's Haidian District.It is one of the largest AI and internet companies in the world. The holding company of the group was incorporated in the Cayman Islands. Baidu was established in 2000 by Robin Li and Eric Xu. Baidu is currently ranked 4th overall in the Alexa Internet rankings.")
company10.save()
company11 =Company.objects.create(company_name="doodle",description="Snicker doodle is very tasty and it's hard to pronounce!")
company11.save()
company12 =Company.objects.create(company_name="dudu",description="Dudu spimds cool.")
company12.save()
company13 =Company.objects.create(company_name="Disney",description="The best paradise in the world!")
company13.save()
company14 =Company.objects.create(company_name="the national museum of american history",description="Are you interested in learning more about the inner workings of history museums? The Smithsonian's National Museum of American History (NMAH) offers formal internships to qualified applicants who are excited to learn!")
company14.save()
company15 =Company.objects.create(company_name="snapchat",description="Snap Inc. is a camera company. We believe that reinventing the camera represents our greatest opportunity to improve the way people live and communicate. Our products empower people to express themselves, live in the moment, learn about the world, and have fun together.")
company15.save()
company16 =Company.objects.create(company_name="riot games",description="The world most famous game: league of legends")
company16.save()
company17 =Company.objects.create(company_name="student organization",description="UCSD student organization, differnet events and opportunities.")
company17.save()
company18 =Company.objects.create(company_name="Nsk Steering Systems America",description="NSK Corporation in Clarinda, Iowa is looking to hire multiple Environmental Health and Safety Interns for our Summer, 2019 program. These are paid positions. The program will run from Mid May through the end of August.")
company18.save()

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
event2.save()
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
event3.save()
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
event4.save()
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
event5.save()
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
event6.save()
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
event7.save()
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
event8.save()
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
event9.save()
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
event10.save()

event11=Event.objects.create(
    event_name="google global business analysis workshop",
    date = "2019-1-12",
    time = "11:30",
    company = company1,
    location = "UCB",
    type = 0,
    description = "Help student get the big picture of google's global business challenges and solutions",
    num_views = 733,
    num_favorites=257)
event11.save()

event12=Event.objects.create(
    event_name="google employees meeting",
    date = "2018-12-13",
    time = "17:30",
    company = company1,
    location = "UCSD",
    type = 0,
    description = "Make friends with google employees and get familiar with the working content at Google",
    num_views = 1023,
    num_favorites=678)
event12.save()

event13=Event.objects.create(
    event_name="Apple art design",
    date = "2018-11-25",
    time = "16:30",
    company = company2,
    location = "UCI",
    type = 1,
    description = "Teach student how to use ipad, iphone to create arts like different drawings",
    num_views = 849,
    num_favorites=685)
event13.save()

event14=Event.objects.create(
    event_name="Apple engineering conference",
    date = "2019-3-22",
    time = "12:30",
    company = company2,
    location = "UCSD",
    type = 0,
    description = "Make students familiar with engineering jobs at Apple and get chance to hand in resumes!",
    num_views = 678,
    num_favorites=567)
event14.save()

event15=Event.objects.create(
    event_name="Apple global business",
    date = "2019-2-17",
    time = "11:30",
    company = company2,
    location = "UCI",
    type = 1,
    description = "Let participants know the challenge of Apple and how to improve the product in global sights!",
    num_views = 789,
    num_favorites=746)
event15.save()

event16=Event.objects.create(
    event_name="Airbnb software engineering meeting",
    date = "2019-2-12",
    time = "7:30",
    company = company9,
    location = "UCD",
    type = 1,
    description = "Practice software engineer's skills and the knowledge you must know in writing software engineer's resume!",
    num_views = 453,
    num_favorites=425)
event16.save()

event17=Event.objects.create(
    event_name="Airbnb hardware engineering meeting",
    date = "2019-2-13",
    time = "7:30",
    company = company9,
    location = "UCSB",
    type = 0,
    description = "Practice hardware engineer's skills and the knowledge you must know in writing hardware engineer's resume!",
    num_views = 474,
    num_favorites=464)
event17.save()

event18=Event.objects.create(
    event_name="Airbnb employee meeting",
    date = "2019-2-14",
    time = "8:30",
    company = company9,
    location = "UCSB",
    type = 0,
    description = "Talk with workers in Airbnb and amplify your network!",
    num_views = 433,
    num_favorites=425)
event18.save()


event19=Event.objects.create(
    event_name="Airbnb employee meeting",
    date = "2019-2-14",
    time = "8:30",
    company = company9,
    location = "UCSB",
    type = 0,
    description = "Talk with workers in Airbnb and amplify your network!",
    num_views = 433,
    num_favorites=425)
event19.save()


event20=Event.objects.create(
    event_name="Airbnb workshop",
    date = "2019-1-3",
    time = "9:15",
    company = company9,
    location = "UCSD",
    type = 1,
    description = "Practice coding and useful tools in engineering!",
    num_views = 637,
    num_favorites=476)
event20.save()


event21=Event.objects.create(
    event_name="facebook coding content",
    date = "2018-12-13",
    time = "9:45",
    company = company4,
    location = "Stanford university",
    type = 0,
    description = "Interesting coding contest for every student to join!",
    num_views = 984,
    num_favorites=869)
event21.save()

event22=Event.objects.create(
    event_name="facebook workshop",
    date = "2018-12-15",
    time = "10:00",
    company = company4,
    location = "Stanford university",
    type = 1,
    description = "Teach how to code and write resume for an internship!",
    num_views = 794,
    num_favorites=453)
event22.save()

event23=Event.objects.create(
    event_name="facebook employee meeting",
    date = "2018-11-18",
    time = "19:30",
    company = company4,
    location = "Stanford university",
    type = 0,
    description = "Meet some employees from facebooks and get chance to hand in resume!",
    num_views = 756,
    num_favorites=671)
event23.save()

event24=Event.objects.create(
    event_name="facebook user experience analysis",
    date = "2018-11-20",
    time = "16:30",
    company = company4,
    location = "UIUC",
    type = 1,
    description = "Learn how to analysis big data in Facebook!",
    num_views = 483,
    num_favorites=912)
event24.save()

event25=Event.objects.create(
    event_name="MBA recruit conference",
    date = "2018-11-25",
    time = "13:30",
    company = company4,
    location = "UCI",
    type = 0,
    description = "If you are a good MBA student, we welcome you to join Facebook for biggest challenge to improve yourself!",
    num_views = 347,
    num_favorites=265)
event25.save()

event26=Event.objects.create(
    event_name="Baidu workshop",
    date = "2018-12-3",
    time = "14:30",
    company = company10,
    location = "Shanghai",
    type = 1,
    description = "Learn how to code elegantly and efficiently!",
    num_views = 674,
    num_favorites=452)
event26.save()

event27=Event.objects.create(
    event_name="Baidu recruit conference",
    date = "2018-12-13",
    time = "15:30",
    company = company10,
    location = "Beijing",
    type = 0,
    description = "Get a chance to get an internship at Baidu!",
    num_views = 512,
    num_favorites=491)
event27.save()

event28=Event.objects.create(
    event_name="Baidu data scientist sharing",
    date = "2018-12-18",
    time = "18:30",
    company = company10,
    location = "Shanghai",
    type = 1,
    description = "Interested in big data analysis, come and listen to Baidu data scientists' sharing!",
    num_views = 632,
    num_favorites=589)
event28.save()

event29=Event.objects.create(
    event_name="Pornhub data analysis",
    date = "2018-12-6",
    time = "8:30",
    company = company3,
    location = "UCSD",
    type = 0,
    description = "Interested in studying people's habit while watching videos, come and listen to pro's talk!",
    num_views = 18273,
    num_favorites=12637)
event29.save()

event30=Event.objects.create(
    event_name="Pornhub free membership",
    date = "2018-12-25",
    time = "9:00",
    company = company3,
    location = "UCSD",
    type = 1,
    description = "Want to get a free membership at Pornhub? Just come and get it!",
    num_views = 102385,
    num_favorites=93872)
event30.save()

event31=Event.objects.create(
    event_name="lol experience sharing",
    date = "2018-12-8",
    time = "21:15",
    company = company16,
    location = "UCSD",
    type = 0,
    description = "Want to know more people who like to play league of legends, come and share!!",
    num_views = 3487,
    num_favorites=2913)
event31.save()

event32=Event.objects.create(
    event_name="lol training",
    date = "2018-11-25",
    time = "20:10",
    company = company16,
    location = "UCSD",
    type = 0,
    description = "Practice your lol skill with many pro players!",
    num_views = 3847,
    num_favorites=3103)
event32.save()

event32=Event.objects.create(
    event_name="china culture sharing",
    date = "2019-3-22",
    time = "4:15",
    company = company17,
    location = "UCSD",
    type = 1,
    description = "Want to learn chinese culture and know people came from China?",
    num_views = 1238,
    num_favorites=984)
event32.save()


event33=Event.objects.create(
    event_name="chinese people study sharing",
    date = "2018-3-23",
    time = "3:15",
    company = company17,
    location = "UCSD",
    type = 0,
    description = "Try to learn how to study fast! And share the tips with others!",
    num_views = 3487,
    num_favorites=2913)
event33.save()


event34=Event.objects.create(
    event_name="cross culture sharing",
    date = "2018-2-17",
    time = "5:50",
    company = company17,
    location = "UCSD",
    type = 1,
    description = "Meet people from different countries and have fun!",
    num_views = 3328,
    num_favorites=1845)
event34.save()


event35=Event.objects.create(
    event_name="cross culture sex party",
    date = "2018-1-1",
    time = "23:50",
    company = company17,
    location = "UCSD",
    type = 0,
    description = "oh yeah, you know what i am talking about!",
    num_views = 1002392,
    num_favorites=983647)
event35.save()


event36=Event.objects.create(
    event_name="Disney global business workshop",
    date = "2018-12-15",
    time = "9:50",
    company = company13,
    location = "UCSD",
    type = 1,
    description = "Study how Disney's business work and change the world!",
    num_views = 7634,
    num_favorites=6734)
event36.save()


event37=Event.objects.create(
    event_name="Disney tech sharing",
    date = "2018-12-20",
    time = "11:50",
    company = company13,
    location = "UCSD",
    type = 0,
    description = "Learn how engineering in Disney support the team and change the world!",
    num_views = 5285,
    num_favorites=4828)
event37.save()

event38=Event.objects.create(
    event_name="Disney global management workshop",
    date = "2019-4-3",
    time = "12:50",
    company = company13,
    location = "UCSD",
    type = 1,
    description = "Learn how Disney manages all employees logically!",
    num_views = 4983,
    num_favorites=4562)
event38.save()

event39 =Event.objects.create(
    event_name="snapchat intern sharing",
    date = "2019-2-21",
    time = "14:45",
    company = company15,
    location = "UCSD",
    type = 0,
    description = "Come and hand in your resume to snapchat employees.",
    num_views = 3726,
    num_favorites=3469)
event39.save()

event40 =Event.objects.create(
    event_name="snapchat tech workshop",
    date = "2019-2-22",
    time = "15:45",
    company = company15,
    location = "UCSD",
    type = 1,
    description = "Learn the newest tech at snapchat.",
    num_views = 3562,
    num_favorites=2761)
event40.save()

event41 =Event.objects.create(
    event_name="snapchat art workshop",
    date = "2019-2-23",
    time = "17:45",
    company = company15,
    location = "UCSD",
    type = 0,
    description = "Learn how to design beautiful front-end by using PHP and html!",
    num_views = 3289,
    num_favorites=2381)
event41.save()

event42 =Event.objects.create(
    event_name="snapchat big data workshop",
    date = "2019-1-28",
    time = "15:15",
    company = company15,
    location = "UCSD",
    type = 1,
    description = "Pro engineers in snapchat teach you how to analyze big data!",
    num_views = 2983,
    num_favorites=2718)
event42.save()

event43 =Event.objects.create(
    event_name="snapchat machine learning workshop",
    date = "2018-12-27",
    time = "20:15",
    company = company15,
    location = "UCSD",
    type = 0,
    description = "Learn how to apply machine learning algorithms in real world!",
    num_views = 5786,
    num_favorites=4785)
event43.save()

event44 =Event.objects.create(
    event_name="snapchat computer vision workshop",
    date = "2018-12-7",
    time = "21:15",
    company = company15,
    location = "UCSD",
    type = 1,
    description = "Learn how to apply computer vision algorithms in real world!",
    num_views = 3289,
    num_favorites=2569)
event44.save()

event45 =Event.objects.create(
    event_name="snapchat educational workshop",
    date = "2018-12-12",
    time = "10:15",
    company = company15,
    location = "UCSD",
    type = 0,
    description = "Help student learn more about snapchat, and know the first-hand information about recruiting!",
    num_views = 2873,
    num_favorites=2465)
event45.save()

event46 =Event.objects.create(
    event_name="snapchat c++ workshop",
    date = "2019-2-7",
    time = "9:20",
    company = company15,
    location = "UCSD",
    type = 1,
    description = "Learn how to correctly program in c++!",
    num_views = 3265,
    num_favorites=2983)
event46.save()


event47 =Event.objects.create(
    event_name="snapchat python workshop",
    date = "2019-2-8",
    time = "9:15",
    company = company15,
    location = "UCSD",
    type = 0,
    description = "Learn how to correctly program in python!",
    num_views = 1092,
    num_favorites=982)
event47.save()


event48 =Event.objects.create(
    event_name="snapchat java workshop",
    date = "2019-2-9",
    time = "9:15",
    company = company15,
    location = "UCSD",
    type = 1,
    description = "Learn how to correctly program in java!",
    num_views = 893,
    num_favorites=782)
event48.save()

event49 =Event.objects.create(
    event_name="snapchat coding contest",
    date = "2019-2-15",
    time = "10:40",
    company = company15,
    location = "UCSD",
    type = 0,
    description = "Attend the most funny coding contest to prove yourself!",
    num_views = 1923,
    num_favorites=1453)
event49.save()

event50 =Event.objects.create(
    event_name="snapchat algorithm conference",
    date = "2019-2-25",
    time = "11:35",
    company = company15,
    location = "UCSD",
    type = 1,
    description = "Dicuss the newest algorithm with professional engineerings in snapchat!",
    num_views = 2156,
    num_favorites=1839)
event50.save()

event51 =Event.objects.create(
    event_name="introduction to oil painting",
    date = "2019-1-7",
    time = "9:20",
    company = company17,
    location = "UCSD",
    type = 0,
    description = "Learn how to draw oil painting, ",
    num_views = 4829,
    num_favorites=3129)
event51.save()

event52 =Event.objects.create(
    event_name="zoo tour guide training",
    date = "2019-2-28",
    time = "8:20",
    company = company17,
    location = "UCSD",
    type = 1,
    description = "Teach you how to get an intern at zoo, learn different knowledges about animals.",
    num_views = 3740,
    num_favorites=1893)
event52.save()

event53 =Event.objects.create(
    event_name="botany learning",
    date = "2019-1-21",
    time = "9:30",
    company = company17,
    location = "UCSD",
    type = 0,
    description = "Want to know more about different plants in ucsd, join us and have fun!",
    num_views = 637,
    num_favorites=541)
event53.save()


event54 =Event.objects.create(
    event_name="car selling conference",
    date = "2019-2-13",
    time = "10:30",
    company = company17,
    location = "UCSD",
    type = 1,
    description = "Come and learn how to be the middle man in selling cars.",
    num_views = 473,
    num_favorites=382)
event54.save()


event55 =Event.objects.create(
    event_name="car selling conference",
    date = "2019-2-13",
    time = "10:30",
    company = company17,
    location = "UCSD",
    type = 1,
    description = "Come and learn how to be the middle man in selling cars.",
    num_views = 473,
    num_favorites=382)
event55.save()

event56 =Event.objects.create(
    event_name="starbuck employee training",
    date = "2018-12-6",
    time = "8:45",
    company = company17,
    location = "UCSD",
    type = 0,
    description = "Learn how to take care of different customers.",
    num_views = 573,
    num_favorites=482)
event56.save()


event57 =Event.objects.create(
    event_name="flower recognition workshop",
    date = "2019-2-11",
    time = "9:00",
    company = company17,
    location = "UCSD",
    type = 1,
    description = "Botany Phd student teaches you how to classify different flowers in the campus!",
    num_views = 475,
    num_favorites=452)
event57.save()

event58 =Event.objects.create(
    event_name="intro to ucsd environment workshop",
    date = "2018-12-11",
    time = "7:15",
    company = company18,
    location = "UCSD",
    type = 0,
    description = "Pro teaches you to understand the environment and how to improve it in ucsd!",
    num_views = 573,
    num_favorites=442)
event58.save()

event59 =Event.objects.create(
    event_name="environment protect workshop",
    date = "2018-12-16",
    time = "9:45",
    company = company18,
    location = "UCSD",
    type = 1,
    description = "Teach you how to protect the environment together and save the resources in daily life.",
    num_views = 374,
    num_favorites=287)
event59.save()

event60 =Event.objects.create(
    event_name="environment clean workshop",
    date = "2018-12-3",
    time = "10:10",
    company = company18,
    location = "UCSD",
    type = 0,
    description = "Learn how to clean and improve our living surroundings every day.",
    num_views = 548,
    num_favorites=348)
event60.save()
