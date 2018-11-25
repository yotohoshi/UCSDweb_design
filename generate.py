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
degree6 = Degree.objects.create(degree="NO LIMITED")
degree6.save()

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
# company1 =Company.objects.create(company_name="Google",description="Google LLC[5] is an American multinational technology company that specializes in Internet-related services and products, which include online advertising technologies, search engine, cloud computing, software, and hardware. Google was founded in 1998 by Larry Page and Sergey Brin while they were Ph.D. students at Stanford University in California. Together they own about 14 percent of its shares and control 56 percent of the stockholder voting power through supervoting stock. They incorporated Google as a privately held company on September 4, 1998. An initial public offering (IPO) took place on August 19, 2004, and Google moved to its headquarters in Mountain View, California, nicknamed the Googleplex. In August 2015, Google announced plans to reorganize its various interests as a conglomerate called Alphabet Inc. Google is Alphabet's leading subsidiary and will continue to be the umbrella company for Alphabet's Internet interests. Sundar Pichai was appointed CEO of Google, replacing Larry Page who became the CEO of Alphabet.")
# company1.save()
# company2 =Company.objects.create(company_name="Apple",description="Apple Inc. is an American multinational technology company headquartered in Cupertino, California, that designs, develops, and sells consumer electronics, computer software, and online services. The company's hardware products include the iPhone smartphone, the iPad tablet computer, the Mac personal computer, the iPod portable media player, the Apple Watch smartwatch, the Apple TV digital media player, and the HomePod smart speaker. Apple's software includes the macOS and iOS operating systems, the iTunes media player, the Safari web browser, and the iLife and iWork creativity and productivity suites, as well as professional applications like Final Cut Pro, Logic Pro, and Xcode. Its online services include the iTunes Store, the iOS App Store and Mac App Store, Apple Music, and iCloud.")
# company2.save()
# company3 =Company.objects.create(company_name="Pornhub",description="Everyone likes it!")
# company3.save()
# company4 =Company.objects.create(company_name="Facebook",description="Facebook, Inc. is an American online social media and social networking service company based in Menlo Park, California. Its website was launched on February 4, 2004, by Mark Zuckerberg, along with fellow Harvard College students and roommates Eduardo Saverin, Andrew McCollum, Dustin Moskovitz and Chris Hughes.")
# company4.save()
# company5 =Company.objects.create(company_name="Amazon",description="Amazon.com, Inc., doing business as Amazon, is an American electronic commerce and cloud computing company based in Seattle, Washington, that was founded by Jeff Bezos on July 5, 1994. The tech giant is the largest Internet retailer in the world as measured by revenue and market capitalization, and second largest after Alibaba Group in terms of total sales.[5] The Amazon.com website started as an online bookstore and later diversified to sell video downloads/streaming, MP3 downloads/streaming, audiobook downloads/streaming, software, video games, electronics, apparel, furniture, food, toys, and jewelry. The company also owns a publishing arm, Amazon Publishing, a film and television studio, Amazon Studios, produces consumer electronics lines including Kindle e-readers, Fire tablets, Fire TV, and Echo devices, and is the world's largest provider of cloud infrastructure services (IaaS and PaaS) through its AWS subsidiary.[6] Amazon also sells certain low-end products under its in-house brand AmazonBasics.")
# company5.save()
# company6 =Company.objects.create(company_name="LinkedIn",description="LinkedIn is a business and employment-oriented service that operates via websites and mobile apps. Founded on December 28, 2002,[4] and launched on May 5, 2003,[5] it is mainly used for professional networking, including employers posting jobs and job seekers posting their CVs. As of 2015, most of the company's revenue came from selling access to information about its members to recruiters and sales professionals.[6] As of October 2018, LinkedIn had 590 million registered members in 200 countries, out of which more than 250 million active users.[3] LinkedIn allows members (both workers and employers) to create profiles and connections to each other in an online social network which may represent real-world professional relationships. Members can invite anyone (whether an existing member or not) to become a connection.[7] The gated-access approach (where contact with any professional requires either an existing relationship or an introduction through a contact of theirs) is intended to build trust among the service's members. LinkedIn participated in the EU's International Safe Harbor Privacy Principles.[8]")
# company6.save()
# company7 =Company.objects.create(company_name="Sensetime",description="SenseTime is a Chinese technology company specializing in artificial intelligence and facial recognition, with offices across China, Hong Kong and Japan. Its products serve over hundreds of well-known companies and government agencies, across a wide range of industries including security, finance, smartphones, mobile Internet, robotics, and automobile.")
# company7.save()
# company8 =Company.objects.create(company_name="Microsoft",description="Microsoft Corporation (MS) is an American multinational technology company with headquarters in Redmond, Washington. It develops, manufactures, licenses, supports and sells computer software, consumer electronics, personal computers, and related services. Its best known software products are the Microsoft Windows line of operating systems, the Microsoft Office suite, and the Internet Explorer and Edge web browsers. Its flagship hardware products are the Xbox video game consoles and the Microsoft Surface lineup of touchscreen personal computers. As of 2016, it is the world's largest software maker by revenue, and one of the world's most valuable companies. The word Microsoft is a portmanteau of microcomputer and software.[5] Microsoft is ranked No. 30 in the 2018 Fortune 500 rankings of the largest United States corporations by total revenue.")
# company8.save()
# company9 =Company.objects.create(company_name="Airbnb",description="Airbnb is a privately held global company headquartered in San Francisco that operates an online marketplace and hospitality service which is accessible via its websites and mobile apps. Members can use the service to arrange or offer lodging, primarily homestays, or tourism experiences. The company does not own any of the real estate listings, nor does it host events; as a broker, it receives commissions from every booking.[3]")
# company9.save()
# company10 =Company.objects.create(company_name="Baidu",description="Baidu, Inc. incorporated on 18 January 2000, is a Chinese multinational technology company specializing in Internet-related services and products and artificial intelligence, headquartered at the Baidu Campus in Beijing's Haidian District.It is one of the largest AI and internet companies in the world. The holding company of the group was incorporated in the Cayman Islands. Baidu was established in 2000 by Robin Li and Eric Xu. Baidu is currently ranked 4th overall in the Alexa Internet rankings.")
# company10.save()
# company11 =Company.objects.create(company_name="doodle",description="Snicker doodle is very tasty and it's hard to pronounce!")
# company11.save()
# company12 =Company.objects.create(company_name="dudu",description="Dudu spimds cool.")
# company12.save()
# company13 =Company.objects.create(company_name="Disney",description="The best paradise in the world!")
# company13.save()
# company14 =Company.objects.create(company_name="the national museum of american history",description="Are you interested in learning more about the inner workings of history museums? The Smithsonian's National Museum of American History (NMAH) offers formal internships to qualified applicants who are excited to learn!")
# company14.save()
# company15 =Company.objects.create(company_name="snapchat",description="Snap Inc. is a camera company. We believe that reinventing the camera represents our greatest opportunity to improve the way people live and communicate. Our products empower people to express themselves, live in the moment, learn about the world, and have fun together.")
# company15.save()
# company16 =Company.objects.create(company_name="riot games",description="The world most famous game: league of legends")
# company16.save()
# company17 =Company.objects.create(company_name="student organization",description="UCSD student organization, differnet events and opportunities.")
# company17.save()
# company18 =Company.objects.create(company_name="Nsk Steering Systems America",description="NSK Corporation in Clarinda, Iowa is looking to hire multiple Environmental Health and Safety Interns for our Summer, 2019 program. These are paid positions. The program will run from Mid May through the end of August.")
# company18.save()

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

###################################################################
print('creating job objects')
job1=Job.objects.create(job_position = "software engineer intern",
    type = 0,
    description = "develop software on different platform",
    company = company1,
    job_URL = "https://careers.google.com/jobs#!t=jo&jid=/google/software-engineering-intern-bs-summer-google-building-c-747-6th-st-south-4235670072&",
    job_duration = "3 month",
    job_location = "mountain view",
    job_Work_Auth = "U.S Citizen",
    #job_paid=1
)
job1.save()
job1.Major_Require.add(major3)
job1.Degree_Require.add(degree3)

job2=Job.objects.create(job_position = "hardware engineer intern",
    type = 1,
    description = "develop hardware on different platform",
    company = company1,
    job_URL = "https://careers.google.com/jobs#!t=jo&jid=/google/hardware-engineering-intern-summer-2019-taipei-taiwan-4565520415&",
    job_duration = "3month",
    job_location = "mountain view",
    job_Work_Auth = "F-1",
    #job_paid=True
)
job2.save()
job2.Major_Require.add(major2)
job2.Degree_Require.add(degree2)

job3=Job.objects.create(job_position = "user experience research intern",
    type = 0,
    description = "see different videos and write down your thought",
    company = company3,
    job_URL = "https://www.pornhub.com/",
    job_duration = "6month",
    job_location = "Canada",
    job_Work_Auth = "F-1",
    #job_paid=True
)
job3.save()
job3.Major_Require.add(major1)
job3.Degree_Require.add(degree1)

job4=Job.objects.create(job_position = "video actor",
    type = 0,
    description = "Actor should perform special behavior with sexy girls.",
    company = company3,
    job_URL = "https://www.pornhub.com/",
    job_duration = "6month",
    job_location = "Canada",
    job_Work_Auth = "F-1",
    #job_paid=True
)
job4.save()
job4.Major_Require.add(major7)
job4.Degree_Require.add(degree3)

job5=Job.objects.create(job_position = "eat eat baby",
    type = 1,
    description = "Dadada dododo dududu doodle.",
    company = company11,
    job_URL = "https://en.wikipedia.org/wiki/Duck",
    job_duration = "3month",
    job_location = "dodadupa",
    job_Work_Auth = "F-1",
    #job_paid=True
)
job5.save()
job5.Major_Require.add(major3)
job5.Degree_Require.add(degree2)

job6=Job.objects.create(job_position = "product manager",
    type = 1,
    description = "help develop products at pornhub, must have lots of experience",
    company = company3,
    job_URL = "https://www.pornhub.com/jobs/job/product-manager/",
    job_duration = "6month",
    job_location = "Montreal",
    job_Work_Auth = "F-1",
    #job_paid=True
)
job6.save()
job6.Major_Require.add(major5)
job6.Degree_Require.add(degree2)

job7=Job.objects.create(job_position = "sucksuck",
    type = 0,
    description = "suck icecream and snacks",
    company = company7,
    job_URL = "https://en.wikipedia.org/wiki/Suck",
    job_duration = "2month",
    job_location = "Shanghai",
    job_Work_Auth = "F-1",
    #job_paid=True
)
job7.save()
job7.Major_Require.add(major3)
job7.Degree_Require.add(degree3)

job8=Job.objects.create(job_position = "boomboomboom",
    type = 1,
    description = "bowbowbow",
    company = company5,
    job_URL = "https://www.youtube.com/watch?v=6QQa7kRnw-0",
    job_duration = "3month",
    job_location = "LA",
    job_Work_Auth = "F-1",
    #job_paid=True
)
job8.save()
job8.Major_Require.add(major9)
job8.Degree_Require.add(degree2)

job9=Job.objects.create(job_position = "boomboompow",
    type = 1,
    description = "bowbowpooooooooooooow",
    company = company9,
    job_URL = "https://www.youtube.com/watch?v=4m48GqaOz90",
    job_duration = "3month",
    job_location = "inyourasshole",
    job_Work_Auth = "F-1",
    #job_paid=True
)
job9.save()
job9.Major_Require.add(major6)
job9.Degree_Require.add(degree2)

job10=Job.objects.create(job_position = "pusher",
    type = 1,
    description = "push people into the car",
    company = company6,
    job_URL = "https://travel.fanpiece.com/globalsavors/%E4%B8%96%E7%95%8C%E4%B8%8A34%E7%A8%AE%E6%9C%80%E5%A5%87%E6%80%AA%E7%9A%84-%E5%86%B7%E9%97%A8-%E8%81%B7%E6%A5%AD-c1117327.html",
    job_duration = "8month",
    job_location = "japan",
    job_Work_Auth = "F-1",
    #job_paid=True
)
job10.save()
job10.Major_Require.add(major2)
job10.Degree_Require.add(degree3)

job11=Job.objects.create(job_position = "research intern",
    type = 0,
    description = "Research happens across Google everyday, in many different teams. Our research has already impacted user-facing services across Google including Search, Maps and Google Now, and is central to the success of Google Cloud and our planet-scale computing, storage, and networking infrastructure.",
    company = company1,
    job_URL = "https://careers.google.com/jobs/results/4643639814586368-research-intern/?category=DATA_CENTER_OPERATIONS&category=DEVELOPER_RELATIONS&category=HARDWARE_ENGINEERING&category=INFORMATION_TECHNOLOGY&category=MANUFACTURING_SUPPLY_CHAIN&category=NETWORK_ENGINEERING&category=PRODUCT_MANAGEMENT&category=PROGRAM_MANAGEMENT&category=SOFTWARE_ENGINEERING&category=TECHNICAL_INFRASTRUCTURE_ENGINEERING&category=TECHNICAL_SOLUTIONS&category=TECHNICAL_WRITING&category=USER_EXPERIENCE&company=Google&company=YouTube&employment_type=INTERN&jlo=en_US",
    job_duration = "6month",
    job_location = "Ann Arbor",
    job_Work_Auth = "F-1",
    #job_paid=True
)
job11.save()
job11.Major_Require.add(major3)
job11.Degree_Require.add(degree1)

job12=Job.objects.create(job_position = "Software Developer Intern",
    type = 1,
    description = "Software Developers at Google are researchers and developers who yearn to create and implement complex computer science solutions. Our developers create massively scalable, distributed software systems and also collaborate on multitudes of smaller projects that have universal appeal - requiring awareness and comprehension of the latest research in the field. We focus on being a collaborative, global organization consisting of developers with the highest levels of technical depth, programming skills and a keen eye for quality.",
    company = company1,
    job_URL = "https://careers.google.com/jobs/results/5201097205284864-software-developer-intern-phd-summer-2019/?category=DATA_CENTER_OPERATIONS&category=DEVELOPER_RELATIONS&category=HARDWARE_ENGINEERING&category=INFORMATION_TECHNOLOGY&category=MANUFACTURING_SUPPLY_CHAIN&category=NETWORK_ENGINEERING&category=PRODUCT_MANAGEMENT&category=PROGRAM_MANAGEMENT&category=SOFTWARE_ENGINEERING&category=TECHNICAL_INFRASTRUCTURE_ENGINEERING&category=TECHNICAL_SOLUTIONS&category=TECHNICAL_WRITING&category=USER_EXPERIENCE&company=Google&company=YouTube&employment_type=INTERN&jlo=en_US",
    job_duration = "3month",
    job_location = "Montreal",
    job_Work_Auth = "F-1",
    #job_paid=True
)
job12.save()
job12.Major_Require.add(major3)
job12.Degree_Require.add(degree2)

job13=Job.objects.create(job_position = "Developer Relations Intern",
    type = 1,
    description = "Passionate people are everywhere at Google. In Developer Relations, we get excited to collaborate and connect with the communities that love technology as much as we do. Part community manager and part developer advocate, Developer Programs Engineers collaborate with developers at conferences and online, and advocate for developers interests internally at Google. Not afraid to be hands-on, you write sample code and client libraries as well as participate in developer forums and support queues to troubleshoot and debug coding problems developers encounter. Internally, you work with product engineering teams improve our products by conveying feedback from developers, reviewing API designs and testing new features. Chrome, Android, App Engine, HTML5 as well as our core G Suite and Ads APIs are just some of the platforms you promote and support.",
    company = company1,
    job_URL = "https://careers.google.com/jobs/results/5163197379969024-developer-relations-intern-summer-2019/?category=DATA_CENTER_OPERATIONS&category=DEVELOPER_RELATIONS&category=HARDWARE_ENGINEERING&category=INFORMATION_TECHNOLOGY&category=MANUFACTURING_SUPPLY_CHAIN&category=NETWORK_ENGINEERING&category=PRODUCT_MANAGEMENT&category=PROGRAM_MANAGEMENT&category=SOFTWARE_ENGINEERING&category=TECHNICAL_INFRASTRUCTURE_ENGINEERING&category=TECHNICAL_SOLUTIONS&category=TECHNICAL_WRITING&category=USER_EXPERIENCE&company=Google&company=YouTube&employment_type=INTERN&jlo=en_US&page=2",
    job_duration = "3month",
    job_location = "New York",
    job_Work_Auth = "F-1",
    #job_paid=True
)
job13.save()
job13.Major_Require.add(major3)
job13.Degree_Require.add(degree2)

job14=Job.objects.create(job_position = "Security Engineer Intern",
    type = 0,
    description = "At Google, our users come first, and the Systems Infrastructure team is at the heart of that promise. We build the technologies that transform the way we think about doing business. Whether working on our cloud systems, researching the latest in computer technology or keeping Google's internal systems humming, Googlers and users alike rely on us to keep things running. We're back-end experts: protecting your privacy and ensuring your security.",
    company = company1,
    job_URL = "https://careers.google.com/jobs/results/4583628799279104-security-engineer-intern-summer-2019/?category=DATA_CENTER_OPERATIONS&category=DEVELOPER_RELATIONS&category=HARDWARE_ENGINEERING&category=INFORMATION_TECHNOLOGY&category=MANUFACTURING_SUPPLY_CHAIN&category=NETWORK_ENGINEERING&category=PRODUCT_MANAGEMENT&category=PROGRAM_MANAGEMENT&category=SOFTWARE_ENGINEERING&category=TECHNICAL_INFRASTRUCTURE_ENGINEERING&category=TECHNICAL_SOLUTIONS&category=TECHNICAL_WRITING&category=USER_EXPERIENCE&company=Google&company=YouTube&employment_type=INTERN&jlo=en_US&page=2",
    job_duration = "3month",
    job_location = "Sunnyvale",
    job_Work_Auth = "F-1",
    #job_paid=True
)
job14.save()
job14.Major_Require.add(major2)
job14.Degree_Require.add(degree1)

job15=Job.objects.create(job_position = "Applications Engineering Intern",
    type = 1,
    description = "As an Applications Engineering Intern, you will play a major role in developing, deploying and supporting Google's internal business applications. You will be tasked with solving various problems over time.",
    company = company1,
    job_URL = "https://careers.google.com/jobs/results/6328535247290368-applications-engineering-intern-summer-2019/?category=DATA_CENTER_OPERATIONS&category=DEVELOPER_RELATIONS&category=HARDWARE_ENGINEERING&category=INFORMATION_TECHNOLOGY&category=MANUFACTURING_SUPPLY_CHAIN&category=NETWORK_ENGINEERING&category=PRODUCT_MANAGEMENT&category=PROGRAM_MANAGEMENT&category=SOFTWARE_ENGINEERING&category=TECHNICAL_INFRASTRUCTURE_ENGINEERING&category=TECHNICAL_SOLUTIONS&category=TECHNICAL_WRITING&category=USER_EXPERIENCE&company=Google&company=YouTube&employment_type=INTERN&jlo=en_US&page=2",
    job_duration = "3month",
    job_location = "Montreal",
    job_Work_Auth = "F-1",
    #job_paid=True
)
job15.save()
job15.Major_Require.add(major3)
job15.Degree_Require.add(degree1)


job16=Job.objects.create(job_position = "Internship opportunities in Marketing for students",
    type = 0,
    description = "What makes Microsoft a great place for marketers? We have amazing products used by billions of people. We have an incredible diversity of businesses. From incumbent brands to challenger brands, and from established markets to emerging markets, we have some of the strongest consumer and enterprise products and services in the world. With an unparalleled depth and breadth of career opportunity and the ability to make a worldwide impact, you can design a career path that is hard to match anywhere. In addition, Microsoft regularly evaluates and evolves the marketing discipline to ensure these roles are designed to increase Microsoft's marketing impact and efficiency while helping our marketing professionals build expertise. ",
    company = company8,
    job_URL = "https://careers.microsoft.com/us/en/job/489152/Internship-opportunities-in-Marketing-for-students",
    job_duration = "2month",
    job_location = "Shanghai",
    job_Work_Auth = "F-1",
    #job_paid=True
)
job16.save()
job16.Major_Require.add(major6)
job16.Degree_Require.add(degree1)

job17=Job.objects.create(job_position = "Internship opportunities in Marketing for MBA students",
    type = 1,
    description = "What makes Microsoft a great place for marketers? We have amazing products used by billions of people. We have an incredible diversity of businesses. From incumbent brands to challenger brands, and from established markets to emerging markets, we have some of the strongest consumer and enterprise products and services in the world. With an unparalleled depth and breadth of career opportunity and the ability to make a worldwide impact, you can design a career path that is hard to match anywhere. In addition, Microsoft regularly evaluates and evolves the marketing discipline to ensure these roles are designed to increase Microsoft's marketing impact and efficiency while helping our marketing professionals build expertise. ",
    company = company8,
    job_URL = "https://careers.microsoft.com/us/en/job/489295/Internship-opportunities-in-Marketing-for-MBA-students",
    job_duration = "3month",
    job_location = "Shanghai",
    job_Work_Auth = "F-1",
    #job_paid=True
)
job17.save()
job17.Major_Require.add(major6)
job17.Degree_Require.add(degree5)

job18=Job.objects.create(job_position = "Marketing Communications Manager (MBA)",
    type = 0,
    description = "We are looking for a seasoned Integrated Marketing Leader to join the Central Marketing Organization (CMO) in a newly expanded leadership role responsible for integrated marketing, marketing communications, and sales enablement specifically working with experiential marketing team for local events and developing local customer evidence to enable vertical selling.",
    company = company8,
    job_URL = "https://careers.microsoft.com/us/en/job/506202/Marketing-Communications-Manager-MBA",
    job_duration = "6month",
    job_location = "Beijing",
    job_Work_Auth = "F-1",
    #job_paid=True
)
job18.save()
job18.Major_Require.add(major6)
job18.Degree_Require.add(degree5)

job19=Job.objects.create(job_position = "Internship opportunities for PhD students & recent graduates: Software Engineering & Program Management",
    type = 1,
    description = "Software engineers at Microsoft are passionate about building technologies that make the world a better place. At Microsoft, you will collaborate with others to solve problems and build some of the world's most advanced services and devices. Your efforts on the design, development, and testing of next-generation applications will have an impact on millions of people. ",
    company = company8,
    job_URL = "https://careers.microsoft.com/us/en/job/486333/Internship-opportunities-for-PhD-students-recent-graduates-Software-Engineering-Program-Management",
    job_duration = "6month",
    job_location = "US",
    job_Work_Auth = "F-1",
    #job_paid=True
)
job19.save()
job19.Major_Require.add(major3)
job19.Degree_Require.add(degree1)


job20=Job.objects.create(job_position = "Intern opportunities for students: User experience",
    type = 0,
    description = "As a user experience expert at Microsoft, you will impact millions of users through innovation and improvement of our software solutions and services. We would like to provide end users an experience that is immersive and pleasing.",
    company = company8,
    job_URL = "https://careers.microsoft.com/us/en/job/473860/Intern-opportunities-for-students-User-experience",
    job_duration = "3month",
    job_location = "US",
    job_Work_Auth = "F-1",
    #job_paid=True
)
job20.save()
job20.Major_Require.add(major3)
job20.Degree_Require.add(degree1)

job21=Job.objects.create(job_position = "Product Manager",
    type = 1,
    description = "As an integral part of the global team working on core products with core technology, Software Technology Center Asia (STCA) plays a significant role contributing to overall Microsoft applications and services products development. It is dedicated to the development for a wide range of Microsoft applications and services products such as Microsoft Office, Office 365, Bing search engine, online advertisement platform, artificial intelligence assistant Cortana and Microsoft XiaoIce, big data, machine learning, speech and natural language processing, as well as internet and mobile related products. Located in Beijing, Suzhou, Taipei and Tokyo, Software Technology Center Asia (STCA) has more than 1000 R&D employees.",
    company = company8,
    job_URL = "https://careers.microsoft.com/us/en/job/495176/Product-Manager",
    job_duration = "6month",
    job_location = "US",
    job_Work_Auth = "F-1",
    #job_paid=True
)
job21.save()
job21.Major_Require.add(major6)
job21.Degree_Require.add(degree1)

job22=Job.objects.create(job_position = "Software Engineering Intern - Core OS",
    type = 0,
    description = "Apple is well known for its innovative products and its pure dedication to customer-oriented features that just work. Behind its success, Apple amasses top engineering talent to develop world-class hardware and software solutions that work amazingly well together.",
    company = company2,
    job_URL = "https://jobs.apple.com/en-us/details/200013120/software-engineering-intern-core-os?team=STDNT",
    job_duration = "3month",
    job_location = "Santa Clara Valley (Cupertino)",
    job_Work_Auth = "F-1",
    #job_paid=True
)
job22.save()
job22.Major_Require.add(major3)
job22.Degree_Require.add(degree1)

job23=Job.objects.create(job_position = "App Store, Apple Music and iTunes Southeast Asia Intern",
    type = 1,
    description = "The App Store is the world's largest and most innovative software store, serving hundreds of millions of iPhone, iPad, Apple TV, Apple Watch, iMessage and Mac customers. We are seeking a dynamic and passionate individual to join us as a Graduate Intern, based in Singapore. You should have a real passion for the digital platform, content and entertainment. You will be participating in a dynamic environment as valuable member of the team, assisting with marketing and business responsibilities to a high standard. The internship will run for 6 months.",
    company = company2,
    job_URL = "https://jobs.apple.com/en-us/details/200010679/app-store-apple-music-and-itunes-southeast-asia-intern?team=STDNT",
    job_duration = "2month",
    job_location = "Singapore",
    job_Work_Auth = "F-1",
    #job_paid=True
)
job23.save()
job23.Major_Require.add(major17)
job23.Degree_Require.add(degree4)

job24=Job.objects.create(job_position = "iTunes Programming Intern (12 months)",
    type = 0,
    description = "The iTunes, Apple Books and App Store teams are looking for fourth-year or post-grad intern that has a real passion for the digital platform, content and/or entertainment. The role is working across the content groups - Music, Books, TV/Movies and Apps - supporting the editorial teams.",
    company = company2,
    job_URL = "https://jobs.apple.com/en-us/details/200010753/itunes-programming-intern-12-months?team=STDNT",
    job_duration = "12month",
    job_location = "Sydney",
    job_Work_Auth = "F-1",
    #job_paid=True
)
job24.save()
job24.Major_Require.add(major3)
job24.Degree_Require.add(degree1)


job25=Job.objects.create(job_position = "Hardware Engineering Internship",
    type = 1,
    description = "Experience Apple. There's the typical job. Punch in, make widgets, punch out, repeat. Then there's a career at Apple. Where you're inspired to defy routine. To explore the far reaches of the possible. To travel unchartered paths. And to be a part of something far bigger than yourself. Because around here, changing the world just comes with the job description. Apple is currently seeking enthusiastic EE major interns who can start work anytime between January 2019 to September 2019. The interns will support electrical & system design and integration of the iPod, iPhone, iPad, Watch and Mac computers. The applicants will assist in engineering processes that support the design, integration, implementation, testing, and qualification of various electrical sub-systems.",
    company = company2,
    job_URL = "https://jobs.apple.com/en-us/details/200011109/hardware-engineering-internship?team=STDNT",
    job_duration = "3month",
    job_location = "Santa Clara Valley (Cupertino)",
    job_Work_Auth = "F-1",
    #job_paid=True
)
job25.save()
job25.Major_Require.add(major1)
job25.Degree_Require.add(degree1)

job26=Job.objects.create(job_position = "Data Scientist Internship - Strategic Data Solutions",
    type = 0,
    description = "Apple's Strategic Data Solutions Analytic Insight team is seeking a Data Scientist Intern for a role this summer at our Austin, Texas location. If you're interested in being a part of a team that's constantly learning and problem-solving, we'd love to talk with you.",
    company = company2,
    job_URL = "https://jobs.apple.com/en-us/details/114266212/data-scientist-internship-strategic-data-solutions?team=STDNT",
    job_duration = "2month",
    job_location = "Austin, Texas",
    job_Work_Auth = "F-1",
    #job_paid=True
)
job26.save()
job26.Major_Require.add(major20)
job26.Degree_Require.add(degree1)

job27=Job.objects.create(job_position = "Environmental Analyst, Intern",
    type = 1,
    description = "Facebook designs, builds, leases and operates the most innovative and efficient data centers in the world. Developing, operating and managing the data center infrastructure and facilities the right way is synonymous with ensuring high uptime, capacity availability, flexibility and capital and operational cost efficiency in a safe working environment. Facebook is seeking an engineer to research and analyze data related to our environmental and water programs for our global data centers. Civil and/or environmental technical expertise as well as research and data visualization skills are required for this position. This position is a full-time 12 week internship located in our Menlo Park headquarters.",
    company = company4,
    job_URL = "https://www.facebook.com/careers/jobs/1761193534002528/",
    job_duration = "3month",
    job_location = "US",
    job_Work_Auth = "F-1",
    #job_paid=True
)
job27.save()
job27.Major_Require.add(major5)
job27.Degree_Require.add(degree1)

job28=Job.objects.create(job_position = "Marketing Science Research Intern",
    type = 0,
    description = "This team is tasked with crafting world-class marketing research for the world's largest marketers. In this role you will pair your analytical skills with Facebook's unique data set to surface insights that help advertisers identify and connect with consumers that matter. ",
    company = company4,
    job_URL = "https://www.facebook.com/careers/jobs/266396807558369/",
    job_duration = "2month",
    job_location = "US",
    job_Work_Auth = "F-1",
    #job_paid=True
)
job28.save()
job28.Major_Require.add(major6)
job28.Degree_Require.add(degree1)

job29=Job.objects.create(job_position = "Client Insights Manager - MBA Intern",
    type = 1,
    description = "This industry-specific, client-facing strategic sales internship is an opportunity to learn deeply about both the Facebook product suite and sales team as well as immerse oneself in a particular industry or sales vertical. This role is responsible for partnering with the existing Facebook sales team mapped to key accounts and enhancing the caliber of this support, with a keen focus on data and insights. Working with the sales team, this Client Insights Manager will analyze and synthesize multiple data sources, including consumer insights, industry and client intelligence, FacebookIQ research, research tools, and industry desk research. They will also package and develop client-specific insights and recommendations through data-driven storytelling, expected to drive impact at a client-specific and Facebook vertical wide level. ",
    company = company4,
    job_URL = "https://www.facebook.com/careers/jobs/336365223838456/",
    job_duration = "2month",
    job_location = "Menlo park",
    job_Work_Auth = "F-1",
    #job_paid=True
)
job29.save()
job29.Major_Require.add(major6)
job29.Degree_Require.add(degree5)

job30=Job.objects.create(job_position = "Research Scientist, Computer Vision (PhD University Grad) 2019",
    type = 0,
    description = "We are seeking world-class computer vision experts to join our teams in developing next generation products and platforms doing research and engineering at scale. We're applying cutting-edge computer vision algorithms to a wide range of media understanding challenges at Facebook. ",
    company = company4,
    job_URL = "https://www.facebook.com/careers/jobs/892283001162100/",
    job_duration = "3month",
    job_location = "Menlo park",
    job_Work_Auth = "F-1",
    #job_paid=True
)
job30.save()
job30.Major_Require.add(major6)
job30.Degree_Require.add(degree5)

job31=Job.objects.create(job_position = "Food & Beverage Quick Service(Part Time)",
    type = 1,
    description = " Cast members in Quick Service Food & Beverage work in fast-paced environments at either counter service or outdoor vending locations. Responsibilities may include taking orders, operating a point-of-sale system (POS register), cash handling, fulfilling orders, food preparation, bussing, general cleaning, stocking items and keeping inventory. Cast members at all of the Quick Service locations, either indoors or outdoors, also interact with guests every day by sharing information, answering questions and providing great guest service!",
    company = company13,
    job_URL = "https://thewaltdisneycompany.dejobs.org/lake-buena-vista-fl/food-beverage-quick-service-part-time-walt-disney-world/BD60E459C26848539225EB72D85AF4D4/job/",
    job_duration = "2month",
    job_location = "Lake Buena Vista,Florida",
    job_Work_Auth = "F-1",
    #job_paid=True
)
job31.save()
job31.Major_Require.add(major22)
job31.Degree_Require.add(degree6)

job32=Job.objects.create(job_position = "HR Business Partner in San Francisco, California",
    type = 0,
    description = "If you have proven experience as an HR Business Partner who thrives in a fast-paced, creative and dynamic environment, while helping deliver HR programs and solutions in support of both short-term and long-term business goals, you've arrived at the right place.",
    company = company13,
    job_URL = "https://thewaltdisneycompany.dejobs.org/san-francisco-ca/hr-business-partner/D99A50B330234EB6809CA5B1E79032D5/job/",
    job_duration = "3month",
    job_location = "San Francisco,California",
    job_Work_Auth = "F-1",
    #job_paid=True
)
job32.save()
job32.Major_Require.add(major6)
job32.Degree_Require.add(degree1)

job33=Job.objects.create(job_position = "Executive Assistant in San Francisco, California",
    type = 1,
    description = "The Executive Assistant provides administrative assistance to the VP, Publicity & Communications at Lucasfilm. The EA is on the front line for public relations and at the center of the PR department. In this position, the EA must be very personable, organized, tech-savvy, and able to multi-task in a fast-paced environment.",
    company = company13,
    job_URL = "https://thewaltdisneycompany.dejobs.org/san-francisco-ca/executive-assistant/B81B9AA2FAC44470A25658672FFB5780/job/",
    job_duration = "2month",
    job_location = "San Francisco,California",
    job_Work_Auth = "F-1",
    #job_paid=True
)
job33.save()
job33.Major_Require.add(major6)
job33.Degree_Require.add(degree1)

job34=Job.objects.create(job_position = "Coordinator, Product Development",
    type = 0,
    description = "Disney is seeking creatives with great ideas, brilliant design talent and passion for innovation. The Product Development Coordinator will help in making sure that our partners develop compelling products and services ensuring creative excellence for the Disney Consumer Products in Southeast Asia. You will be reporting to the Creative & Product Development Lead - Disney Consumer Products. Join the worlds #1 Entertainment brand and 'Be Part of the Story'.",
    company = company13,
    job_URL = "https://thewaltdisneycompany.dejobs.org/singapore-sgp/coordinator-product-development-12-months-contract/B47E8054C46641DD81214168B6498B40/job/",
    job_duration = "12month",
    job_location = "Singapore,Singapore",
    job_Work_Auth = "F-1",
    #job_paid=True
)
job34.save()
job34.Major_Require.add(major6)
job34.Degree_Require.add(degree5)


job35=Job.objects.create(job_position = "Art Lead in Glendale",
    type = 1,
    description = "The Art Lead will work closely with the Executive Creative Director and Art Director to creatively manage the visual development of multiple licensed titles, provide visual guidance and brand feedback, help our partners define each project's style parameters, and to maintain and push our quality standards on the games across our diverse and growing portfolio of mobile, VR, and console games.",
    company = company13,
    job_URL = "https://thewaltdisneycompany.dejobs.org/glendale-ca/art-lead/CD29520B94C14D52BE076B6851DD1F01/job/",
    job_duration = "5month",
    job_location = "Glendale,California",
    job_Work_Auth = "F-1",
    #job_paid=True
)
job35.save()
job35.Major_Require.add(major17)
job35.Degree_Require.add(degree1)


job36=Job.objects.create(job_position = "Sr Copywriter in Celebration",
    type = 0,
    description = "Concept and create highly engaging advertising and integrated campaigns. Must be digital and social savvy. Strategically strong and able to work with multi-disciplinary internal teams to ensure smart, on brand work. Review and present work with internal leadership and external partners. Collaborate with and at times lead outside agency and production partners on projects. Mentor junior teams. Must be self-directed and able to work in a fast paced, high volume, deadline driven environment. Must like to have fun and be award hungry.",
    company = company13,
    job_URL = "https://thewaltdisneycompany.dejobs.org/celebration-fl/sr-copywriter/C2C1CFBEFB8F4EA28102F02D745FF301/job/",
    job_duration = "3month",
    job_location = "Celebration,Florida",
    job_Work_Auth = "F-1",
    #job_paid=True
)
job36.save()
job36.Major_Require.add(major17)
job36.Degree_Require.add(degree1)


job37=Job.objects.create(job_position = "Senior Production Artisan in Anaheim",
    type = 1,
    description = "Those in this position are expected to contribute fabrication techniques and structural necessities with fellow team members to realize finished products. This creative work involves the use of all manner of materials and tools to fabricate and maintain live-entertainment assets including the following disciplines:- carpentry, estimating, scenic painting, sculpting, textiles, puppetry, sign fabrication and properties construction.",
    company = company13,
    job_URL = "https://thewaltdisneycompany.dejobs.org/anaheim-ca/senior-production-artisan/F0983634FED949728D1165B08BB31B18/job/",
    job_duration = "4month",
    job_location = "Anaheim,California",
    job_Work_Auth = "F-1",
    #job_paid=True
)
job37.save()
job37.Major_Require.add(major21)
job37.Degree_Require.add(degree4)

job38=Job.objects.create(job_position = "Group Creative Director in Glendale",
    type = 0,
    description = "The Digital Group Creative Director reports to the Director, Digital Creative and assists with daily leadership on client business. She/He will be instrumental in guiding and managing the creative team, upholding creative vision and generating work to maintain Disney Yellow Shoes standards, and will utilize insights to develop concepts and give creative guidance. The Digital Group Creative Director should be a source of inspiration for the team and must be a highly organized time manager, problem solver, originator of process, partner to the Acct Management team, client partner, team morale booster, a great communicator and listener. The Digital Group Creative Director is expected to think creatively in all aspects of the role. The candidate will play a pivotal role in driving the digital creative output of the agency forward. He/she will work alongside the Director, Digital Creative and be a positive role model to all members of the agency team.",
    company = company13,
    job_URL = "https://thewaltdisneycompany.dejobs.org/glendale-ca/group-creative-director/97C30553B82B4570BCBC36F16E11CB85/job/",
    job_duration = "6month",
    job_location = "Glendale,California",
    job_Work_Auth = "F-1",
    #job_paid=True
)
job38.save()
job38.Major_Require.add(major21)
job38.Degree_Require.add(degree4)

job38=Job.objects.create(job_position = "Community Journalist",
    type = 1,
    description = "You will be expected to produce various styles for various platforms. You must be able to research, set-up, shoot, edit, and write content on a daily basis. Experience with Adobe Premiere and/or Dalet One-Cut is a plus.We want respected, knowledgeable, and ethical station representatives. You must be willing to be assigned to live in a specific community in order to cultivate contacts and root-out great, exclusive, unique local stories and you must be willing to work any day, any shift.",
    company = company13,
    job_URL = "https://thewaltdisneycompany.dejobs.org/new-york-ny/community-journalist/8265DC53BC1044E680B43C60BDB3E504/job/",
    job_duration = "4month",
    job_location = "New York,New York",
    job_Work_Auth = "F-1",
    #job_paid=True
)
job38.save()
job38.Major_Require.add(major8)
job38.Degree_Require.add(degree6)

job39=Job.objects.create(job_position = "Learning Partner",
    type = 0,
    description = "An opportunity with Disney English allows you to make a difference in the lives of children, all while receiving ongoing professional development and gaining valuable experience within The Walt Disney Company. Become one Disney English cast member could be the experience of a lifetime. Bring your talent, creativity and unique experience, and discover why a career with Disney is the opportunity you've been looking for.",
    company = company13,
    job_URL = "https://thewaltdisneycompany.dejobs.org/beijing-chn/learning-partner-beijing/A7481E6EA18345ADA5CFA0E566F3A4C7/job/",
    job_duration = "8month",
    job_location = "Beijing, China",
    job_Work_Auth = "F-1",
    #job_paid=True
)
job39.save()
job39.Major_Require.add(major8)
job39.Degree_Require.add(degree1)

job40=Job.objects.create(job_position = "ILMxLAB Gameplay Engineer San Francisco",
    type = 0,
    description = "We're on a mission: building the future. We're working in this crazy-fun, hybridized fusion of entertainment where exceptionally high-end (previously pre-rendered) VFX meets interactive, immersive stories. That spectacular mash-up results in unparalleled real-time worlds where we endeavor to raise the bar for experiences and visuals as high as we possibly can. As if making compelling movies and games wasn't hard enough in isolation! Don't get us wrong, we're not complaining about the challenges. That's literally why we come to work: It is our great fortune to be standing at the crossroads - unconstrained by a specific title or universe - in a collaborative, highly creative and highly technical work environment. If that sounds interesting, jump in. We still believe in picking up hitchhikers.",
    company = company13,
    job_URL = "https://thewaltdisneycompany.dejobs.org/san-francisco-ca/ilmxlab-gameplay-engineersan-francisco-ca/899686A5D92342F6AC1670DA53A413F8/job/",
    job_duration = "3month",
    job_location = "San Francisco,California",
    job_Work_Auth = "F-1",
    #job_paid=True
)
job40.save()
job40.Major_Require.add(major23)
job40.Degree_Require.add(degree1)

job41=Job.objects.create(job_position = "Data Scientist, Intern 2019 - Algorithms",
    type = 1,
    description = "Here at Airbnb, we're big fans of travel. We love thinking about the diversity of experiences our host community offers, and we spend a fair amount of time trying to make sense of the tens of thousands of cities where people are booking trips every night. The tricky thing is, most of us haven't been to Cuba, so we try to come up with creative ways to help people find the experience they're looking for in places they may have never been.  The data science team works in tandem with product management, engineering, and design teams to solve these types of technical challenges.",
    company = company9,
    job_URL = "https://zh-t.airbnb.com/careers/departments/position/1385868",
    job_duration = "2month",
    job_location = "San Francisco,California",
    job_Work_Auth = "F-1",
    #job_paid=True
)
job41.save()
job41.Major_Require.add(major20)
job41.Degree_Require.add(degree1)

job42=Job.objects.create(job_position = "Data Scientist, Intern 2019 - Analytics",
    type = 0,
    description = "Here at Airbnb, we're big fans of travel.  We love thinking about the diversity of experiences our host community offers, and we spend a fair amount of time trying to make sense of the tens of thousands of cities where people are booking trips every night. The tricky thing is, most of us haven't been to Cuba, so we try to come up with creative ways to help people find the experience they're looking for in places they may have never been.  The data science team works in tandem with product management, engineering, and design teams to solve for things like this.",
    company = company9,
    job_URL = "https://zh-t.airbnb.com/careers/departments/position/1385841",
    job_duration = "3month",
    job_location = "San Francisco, United States",
    job_Work_Auth = "F-1",
    #job_paid=True
)
job42.save()
job42.Major_Require.add(major20)
job42.Degree_Require.add(degree1)

job43=Job.objects.create(job_position = "Data Scientist, New Grad 2019 - Inference",
    type = 1,
    description = "Here at Airbnb, we're big fans of travel.  We love thinking about the diversity of experiences our host community offers, and we spend a fair amount of time trying to make sense of the tens of thousands of cities where people are booking trips every night. The tricky thing is, most of us haven't been to Cuba, so we try to come up with creative ways to help people find the experience they're looking for in places they may have never been.  The data science team works in tandem with product management, engineering, and design teams to solve for things like this.",
    company = company9,
    job_URL = "https://zh-t.airbnb.com/careers/departments/position/1385914",
    job_duration = "3month",
    job_location = "San Francisco, United States",
    job_Work_Auth = "F-1",
    #job_paid=True
)
job43.save()
job43.Major_Require.add(major20)
job43.Degree_Require.add(degree1)


job44=Job.objects.create(job_position = "Software Engineer, New Grad 2019",
    type = 0,
    description = "Here at Airbnb, we're big fans of travel.  We love thinking about the diversity of experiences our host community offers, and we spend a fair amount of time trying to make sense of the tens of thousands of cities where people are booking trips every night. The tricky thing is, most of us haven't been to Cuba, so we try to come up with creative ways to help people find the experience they're looking for in places they may have never been.  The data science team works in tandem with product management, engineering, and design teams to solve for things like this.",
    company = company9,
    job_URL = "https://zh-t.airbnb.com/careers/departments/position/1280332",
    job_duration = "6month",
    job_location = "Portland, United States",
    job_Work_Auth = "F-1",
    #job_paid=True
)
job44.save()
job44.Major_Require.add(major3)
job44.Degree_Require.add(degree1)


job45=Job.objects.create(job_position = "User Experience Designer, Intern",
    type = 1,
    description = "We are looking for a User Experience Designer, Intern to join our team. In this role, you will be responsible for creating innovative end-to-end user experiences for existing and new product offerings, collaborating with product managers to define the interaction design of products and visualizing new concepts.",
    company = company6,
    job_URL = "https://www.linkedin.com/jobs/view/969796886/",
    job_duration = "4month",
    job_location = "Sunnyvale, CA, US",
    job_Work_Auth = "F-1",
    #job_paid=True
)
job45.save()
job45.Major_Require.add(major17)
job45.Degree_Require.add(degree4)


job46=Job.objects.create(job_position = "Site Reliability Engineers",
    type = 0,
    description = "Fill the mission-critical role of ensuring that our complex, large-scale systems are healthy, monitored, automated, and designed to scale. You'll use your interest in site operations and your experience writing code to work closely with our development teams from the early stages of design all the way through identifying and resolving production issues.",
    company = company6,
    job_URL = "https://careers.linkedin.com/students/Internships/Technical",
    job_duration = "12month",
    job_location = "US",
    job_Work_Auth = "F-1",
    #job_paid=True
)
job46.save()
job46.Major_Require.add(major2)
job46.Degree_Require.add(degree1)

job47=Job.objects.create(job_position = "Systems and Infrastructure Engineer",
    type = 1,
    description = "Scale LinkedIn's infrastructure to handle massive growth in membership, traffic, and data as we continue to experience dramatic growth in the usage of our products with a focus in Data Infrastructure, Search, Network and Analytics Platforms, Service Platforms and Systems/Algorithms that generate relevant Content and Community.",
    company = company6,
    job_URL = "https://careers.linkedin.com/students/Internships/Technical",
    job_duration = "12month",
    job_location = "US",
    job_Work_Auth = "F-1",
    #job_paid=True
)
job47.save()
job47.Major_Require.add(major15)
job47.Degree_Require.add(degree1)


job48=Job.objects.create(job_position = "Systems and Infrastructure Engineer",
    type = 0,
    description = "Manage and drive global product requirements, develop end-to-end project plans, and lead functional and technical delivery of key team-, org-, and company-wide initiatives. Work with the product development team and other cross-functional teams to bring product features live to the site.",
    company = company6,
    job_URL = "https://careers.linkedin.com/students/Internships/Technical",
    job_duration = "12month",
    job_location = "US",
    job_Work_Auth = "F-1",
    #job_paid=True
)
job48.save()
job48.Major_Require.add(major1)
job48.Degree_Require.add(degree1)


job49=Job.objects.create(job_position = "Machine Learning and Relevance",
    type = 1,
    description = "Work on our massive semi-structured text, graph and user activity data sets. Build highly scalable, highly performant social graph engines, state-of-the-art full-text search engines, and platforms for recommendation and applied data analytics. You will utilize data mining, information retrieval, machine learning and perfect your strong systems orientation skills. ",
    company = company6,
    job_URL = "https://careers.linkedin.com/students/Internships/Technical",
    job_duration = "12month",
    job_location = "US",
    job_Work_Auth = "F-1",
    #job_paid=True
)
job49.save()
job49.Major_Require.add(major3)
job49.Degree_Require.add(degree4)


job50=Job.objects.create(job_position = "GM , Global Catalog Business Development, AWS Marketplace & Service Catalog",
    type = 1,
    description = "Amazon Web Services (AWS) is a dynamic and rapidly growing business within Amazon and the leader in providing secure, reliable, scalable, and innovative cloud services that help millions of customers across the globe scale and grow! As part of these services, AWS provides innovate ways for customers to modernize and manage their applications as part of migration to cloud. AWS Marketplace & Service Catalog are two services built to enable procurement, provisioning and governance of third party software to be run on AWS. The business works with over 1,300 software vendors, has over 190,000 active customers, and runs globally.",
    company = company5,
    job_URL = "https://www.amazon.jobs/en/jobs/724430/gm-global-catalog-business-development-aws-marketplace-service-catalog",
    job_duration = "12month",
    job_location = "Seattle, Washington",
    job_Work_Auth = "F-1",
    #job_paid=True
)
job50.save()
job50.Major_Require.add(major6)
job50.Degree_Require.add(degree1)


job51=Job.objects.create(job_position = "Bus Dev Manager - Amazon Locker / Pick-Up",
    type = 0,
    description = "Meet the Amazon Access Points team. We are transforming how quickly and conveniently Amazon delivers to its customers. Amazon Locker & Pickup delight customers by providing safe, secure and convenient pickup and returns options. We leverage these capabilities to delight more customers and create new business. In the same manner in which Amazon Web Services (AWS) leveraged Amazon's IT infrastructure, we leverage our operations and transportation infrastructure to create new startup businesses like Amazon lockers (amazon.com/lockers).",
    company = company5,
    job_URL = "https://www.amazon.jobs/en/jobs/749425/bus-dev-manager-amazon-locker-pick-up",
    job_duration = "1month",
    job_location = "Seattle, Washington",
    job_Work_Auth = "F-1",
    #job_paid=True
)
job51.save()
job51.Major_Require.add(major6)
job51.Degree_Require.add(degree1)


job52=Job.objects.create(job_position = "Partner Development Representative",
    type = 1,
    description = "Come and join Amazon Web Services (AWS) as we redefine the IT Industry. We are building a business that has the potential to be at least as big as the Amazon.com retail business and are seeking world class candidates to contribute to this effort. As a Partner Development Representative, you will have the exciting opportunity to recruit, enable and grow our ecosystem of Amazon Partner Network (APN) Partners. These partners consist of some of the most innovative Independent Software Vendors (ISVs), SaaS and PaaS providers, as well as trusted Systems Integrators, Managed Service Providers and Consultants.",
    company = company5,
    job_URL = "https://www.amazon.jobs/en/jobs/749973/partner-development-representative",
    job_duration = "2month",
    job_location = "Seattle, Washington",
    job_Work_Auth = "F-1",
    #job_paid=True
)
job52.save()
job52.Major_Require.add(major6)
job52.Degree_Require.add(degree4)


job53=Job.objects.create(job_position = "Expansion Transaction Manager",
    type = 0,
    description = "A successful candidate will be an exceptional communicator with both vendors and internal customers, have a strong ability to overcome obstacles to deliver the right results, possess a strong sense of ownership, be adept at taking calculated risks in order to act quickly, have strong organizational skills, and be data driven with a passion for continuous improvement. This position involves direct contact with senior leaders and key vendors; you must have a professional demeanor and be able to communicate effectively with people at every level, both internally and externally.",
    company = company5,
    job_URL = "https://www.amazon.jobs/en/jobs/749359/expansion-transaction-manager",
    job_duration = "4month",
    job_location = "Seattle, Washington",
    job_Work_Auth = "F-1",
    #job_paid=True
)
job53.save()
job53.Major_Require.add(major6)
job53.Degree_Require.add(degree1)



job54=Job.objects.create(job_position = "Art Director, New World",
    type = 1,
    description = "At Amazon, we believe the evolution that began with arcade communities a quarter at a time, growing to the massively shared live streams and online experiences of today, will continue to a future where everyone is a gamer, and every gamer can create, compete, collaborate and connect with others at massive scales. If you share our belief that games will produce some of the future's most influential voices in media and art, come join us! We are looking for an Art Director to join our New World team at Amazon Game Studios, Orange County. New World is a Sandbox MMO set in an alternate version of the 17th Century. As New World's Art Director you will guide the artistic vision. You will lead a team of artists to push the aesthetic. You will help define the experience of New World from launch through years of live service enhancements and updates.",
    company = company5,
    job_URL = "https://www.amazon.jobs/en/jobs/738955/art-director-new-world",
    job_duration = "3month",
    job_location = "Southern California Region, CaliforniaIrvine, CA",
    job_Work_Auth = "F-1",
    #job_paid=True
)
job54.save()
job54.Major_Require.add(major17)
job54.Degree_Require.add(degree4)

job55=Job.objects.create(job_position = "Creative Director",
    type = 0,
    description = "IMDb is the world's most popular and authoritative source for movie, TV, and celebrity content, reaching an audience of more than 250 million unique visitors per month. IMDbPro, our professional subscription business, is transforming the business of entertainment. Our mission is to inform and connect professionals in the entertainment industry to help them do their jobs better and advance their careers.",
    company = company5,
    job_URL = "https://www.amazon.jobs/en/jobs/743110/creative-director",
    job_duration = "2month",
    job_location = "Southern California Region, CaliforniaIrvine, CA",
    job_Work_Auth = "F-1",
    #job_paid=True
)
job55.save()
job55.Major_Require.add(major17)
job55.Degree_Require.add(degree4)


job56=Job.objects.create(job_position = "Environment Artist - New World",
    type = 1,
    description = "New World is a massively multiplayer, open-ended sandbox game that allows you to carve your own destiny with other players in a living, hostile, cursed land. How you play, what you do, and whom you work with or against is up to you. Live on your own amidst the supernatural terrors or join with others to build thriving civilizations. In this evolving world that transforms with the changing of the seasons, weather, and time of day, the only limit is your own ambition.",
    company = company5,
    job_URL = "https://www.amazon.jobs/en/jobs/746593/environment-artist-new-world",
    job_duration = "3month",
    job_location = "Southern California Region, CaliforniaIrvine, CA",
    job_Work_Auth = "F-1",
    #job_paid=True
)
job56.save()
job56.Major_Require.add(major5)
job56.Degree_Require.add(degree4)

job57=Job.objects.create(job_position = "history internship",
    type = 0,
    description = "All Smithsonian internships are prearranged, structured learning experiences that take place within a specific time period, usually fall, spring and summer each year. Each internship should be relevant both to the intern's academic and professional goals and to the professional disciplines represented at the museum.",
    company = company14,
    job_URL = "http://americanhistory.si.edu/getinvolved/internship",
    job_duration = "2month",
    job_location = "US",
    job_Work_Auth = "F-1",
    #job_paid=True
)
job57.save()
job57.Major_Require.add(major19)
job57.Degree_Require.add(degree4)


job58=Job.objects.create(job_position = "Internal Events Coordinator",
    type = 1,
    description = "We're looking for an Internal Events Coordinator to join Snap Inc! As part of the Internal Events team, you'll assist with the planning and development of special events that enrich our company culture as we scale. This role is based in our Santa Monica, CA headquarters.",
    company = company15,
    job_URL = "https://boards.greenhouse.io/snapchat/jobs/1412691",
    job_duration = "2month",
    job_location = "Los Angeles, CA",
    job_Work_Auth = "F-1",
    #job_paid=True
)
job58.save()
job58.Major_Require.add(major24)
job58.Degree_Require.add(degree4)


job59=Job.objects.create(job_position = "Producer, Creator Stories",
    type = 0,
    description = "We're looking for a Producer, Creator Stories to join Team Snapchat! As a member of the Content team, you will help create and execute the programming strategy for creator-led content on Snapchat. Working from our Los Angeles, CA headquarters, you'll collaborate with our Content team to help develop and execute programming strategy.",
    company = company15,
    job_URL = "https://boards.greenhouse.io/snapchat/jobs/1418957",
    job_duration = "3month",
    job_location = "Los Angeles, CA",
    job_Work_Auth = "F-1",
    #job_paid=True
)
job59.save()
job59.Major_Require.add(major6)
job59.Degree_Require.add(degree1)

job60=Job.objects.create(job_position = "Executive Assistant",
    type = 1,
    description = "We're looking for an Executive Assistant to join Snap Inc! You'll be responsible for scheduling, coordinating team events, and generally helping us stay ten steps ahead. We are looking for someone who thrives supporting multiple executives in a fast-paced environment. In addition to being organized, analytical, and resourceful, you must possess strong business judgment and communication skills needed to interact with a variety of people and job functions. High enthusiasm, creativity, and resourcefulness are crucial, as is a high level of professional integrity and confidentiality.",
    company = company15,
    job_URL = "https://boards.greenhouse.io/snapchat/jobs/1209013",
    job_duration = "2month",
    job_location = "Los Angeles, CA",
    job_Work_Auth = "F-1",
    #job_paid=True
)
job60.save()
job60.Major_Require.add(major6)
job60.Degree_Require.add(degree5)