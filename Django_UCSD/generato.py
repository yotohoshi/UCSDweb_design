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
#print("start")


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
company19 =Company.objects.create(company_name="world bank group",description="A strong and engaged private sector is indispensable to ending extreme poverty and boosting shared prosperity. That's where IFC comes in-we have more than 60 years of experience in unlocking private investment, creating markets and opportunities where they're needed most. Since 1956, IFC has leveraged $2.6 billion in capital to deliver more than $265 billion in financing for businesses in developing countries.")
company19.save()
company20 =Company.objects.create(company_name="IBM",description="The company began in 1911 as the Computing-Tabulating-Recording Company (CTR) and was renamed International Business Machines in 1924. IBM manufactures and markets computer hardware, middleware and software, and provides hosting and consulting services in areas ranging from mainframe computers to nanotechnology.")
company20.save()
company21 =Company.objects.create(company_name="ucsd",description="our school")
company21.save()
company22 =Company.objects.create(company_name="ebay",description="useful online shop")
company22.save()




event1=Event.objects.create(
    event_name="2018 World Bank Group Youth Summit: Unleashing the Power of Human Capital",
    date = "2018-12-3",
    time = "9:00",
    company = company19,
    location = "Washington",
    type = 0,
    description = "The WBG Youth Summit is the largest annual gathering of global youth at the World Bank. The primary goal of the Summit is to empower youth to find their own innovative ideas for development and provide a platform for dialogue between youth, the WBG, and the international community. The event has been organized since 2013, each year having a different theme including governance, climate change, education and most recently, technology and innovation. The 2017 Summit engaged over 400 participants, attracted over 12,500 viewers online and received 500 competition entries from more than 150 countries. The sixth annual WBG Youth Summit will be held at the World Bank in Washington D.C. on December 3rd-4th, 2018. The two-day summit will contain plenary sessions to engage youth with thought-leaders in human capital and workshops to provide youth attendees with the opportunity to share ideas and discuss. An important element of the Summit is the Competition which will invite young professionals to submit business or policy level proposals on the year's topic. Registration for the competition and attendance to the Summit is now open. THE DEADLINE TO APPLY IS OCTOBER 5, 2018. A key determinant of a country's competitiveness is its human talent - the skills, knowledge, and experience of its population, better known as 'human capital'. The agenda of this year's Youth Summit will be structured around two main sub-themes, exploring how youth can maximize their, and other individuals', human capital throughout their lifespan. The event is open for youth ages 18-35 so is applicable for both undergraduate and graduate students while also attracting many young professionals. We can also work with you to arrange a remote watch party as the event will be livestreamed. ",
    num_views = 12032,
    num_favorites=8473)
event1.save()
event2=Event.objects.create(
    event_name="IBM Virtual Office Hours",
    date = "2018-12-4",
    time = "18:00",
    company = company20,
    location = "ucsd",
    type = 1,
    description = "Curious to know what it's like to work at IBM? Chat virtually with two of IBM's Campus Ambassador's, who just completed a technical summer internship at IBM! Visit the following link on December 4th, between 6-8pm PST, to chat with Shirley and Mark! https://app.brazenconnect.com/a/-IBM-/e/4LQbp Come prepared with questions related around IBM's work culture, team projects, work life balance, and more! Be sure to also join our Talent Network: https://ibm.co/TalentNetwork_UCSD .",
    num_views = 8594,
    num_favorites=3897)
event2.save()
event3=Event.objects.create(
    event_name="Writing the Cover Letter: Webinar Mini-Tutorial (for Master's & PhD Students)",
    date = "2018-12-15",
    time = "12:00",
    company = company21,
    location = "ucsd",
    type = 0,
    description = "***Online webinar; link will be emailed to those who RSVP at least 24 hours prior to the webinar. Missed the cover letter workshop for graduate students earlier this quarter, or just want a refresher? This webinar will provide an overview of the top tips for writing a winning cover letter.",
    num_views = 6578,
    num_favorites=2567)
event3.save()
event4=Event.objects.create(
    event_name="The Job Search, for International Master's and PhD Students",
    date = "2018-12-17",
    time = "12:00",
    company = company21,
    location = "ucsd, career center",
    type = 1,
    description = "While finding a job in the United States is rarely easy, unstated expectations and hidden customs can make it even harder for international applications. This workshop aims to elucidate those quirks of U.S. businesses while assisting attendees in formulating a strategy for approaching the job search. This workshop is targeted at International Master's and PhD students, but any graduate student may attend.",
    num_views = 6498,
    num_favorites=2390)
event4.save()
event5=Event.objects.create(
    event_name="THE NEXT GENERATION OF INVESTING #MILLENNIALTOUCH",
    date = "2019-1-15",
    time = "11:00",
    company = company21,
    location = "ucsd, career center",
    type = 0,
    description = "TRITON FUNDS is a student-driven initiative created to provide real-life opportunities that not only produce excellent returns, but also strengthen the community. By utilizing alternative investment strategies with a millennial outlook, we help stand still businesses emerge into industry leaders. Our growth driven cycle yields efficient advancements for students, investors, companies, and the community. Meet and Greet the Triton Funds - students in leadership.",
    num_views = 5896,
    num_favorites=1893)
event5.save()
event6=Event.objects.create(
    event_name="Meet Paul Founder of -Ancestry.com and Soar",
    date = "2019-1-8",
    time = "16:30",
    company = company21,
    location = "ucsd, career center",
    type = 0,
    description = "Meet Paul Allen, best known for founding Ancestry.com in 1997 (now worth 2.6 Billion) and now Soar.com. Paul will talk about how he connected to our past by founding Ancestry.com and how we can connect to our future by becoming the world's foremost thought leader on the Strengths Movement. Listen to how Paul is on a mission to help every student, executive, team, and company understand their unique abilities in order to uplift humanity.",
    num_views = 3478,
    num_favorites=1453)
event6.save()
event7=Event.objects.create(
    event_name="Triage Consulting Group Informational Session",
    date = "2019-1-15",
    time = "18:00",
    company = company21,
    location = "ucsd, career center",
    type = 1,
    description = "Triage Consulting Group will be hosting an Info Session on campus on Tuesday, 1/15 at 6pm!Triage Consulting Group is a San Francisco and Atlanta-based financial healthcare consulting firm specializing in the needs of hospitals in today's dynamic healthcare industry. Through on and off-site consulting, Triage works to maximize cash flow and provide the necessary training for future revenue enhancement. Since its inception in 1994, Triage has identified and recovered over $4 billion in lost revenue at more than 700 hospitals. Our clients include some of the largest hospitals and healthcare systems in the United States. Triage is currently looking to hire entry level Associate Consultants for its San Francisco office among students graduating this year.",
    num_views = 2367,
    num_favorites=1321)
event7.save()
event8=Event.objects.create(
    event_name="2019 Triton Winter Career Fair",
    date = "2019-1-16",
    time = "10:00",
    company = company22,
    location = "ucsd, price senter",
    type = 1,
    description = "It's never too early (or late) to explore career opportunities! The Career Center's Industry Engagement Team works with leading employers from every industry to bring internship and job opportunities to students and alumni through Career Fairs. Attend UC San Diego Career Fairs where you can meet with employers face-to-face.",
    num_views = 1567,
    num_favorites=1023)
event8.save()
event9=Event.objects.create(
    event_name="Peace Corps Information Session",
    date = "2019-1-24",
    time = "17:00",
    company = company21,
    location = "ucsd, career center",
    type = 1,
    description = "Serving in the Peace Corps is a great way to immerse yourself in a new culture, learn a new language, and have the experience of a lifetime. Join us at this information session to learn about Volunteer experiences, ask questions about service, and gain tips to guide you through the application process.",
    num_views = 894,
    num_favorites=578)
event9.save()

event10=Event.objects.create(
    event_name="2019 Entrepreneurship Certificate Program",
    date = "2019-1-15",
    time = "14:00",
    company = company21,
    location = "ucsd, career center",
    type = 1,
    description = "For more information: Please email gsands@ucsd.edu Do you have an IDEA for a product, solution or business? Do you want to make an impact? Where do you start? Join the next session of the 8-week Entrepreneurship Certificate Program. Hear from experienced practitioners about developing ideas, forming a business, and starting your innovation journey. The next session starts Tuesday, January 15, 2019 - 2pm, at the Career Services Center's Horizon Room.",
    num_views = 322,
    num_favorites=133)
event10.save()

event11=Event.objects.create(
    event_name="Graduate Student Lunch & Learn: Social Media Workshop",
    date = "2019-1-25",
    time = "12:00",
    company = company21,
    location = "ucsd, career center",
    type = 0,
    description = "Junior high tweet haunting your interviews? Come to the Graduate Social Media Workshop, where you'll learn how to privatize your social media accounts, delete those Facebook arguments with your uncle, and look professional online. Lunch will be provided, so please make sure to RSVP!",
    num_views = 733,
    num_favorites=257)
event11.save()

event12=Event.objects.create(
    event_name="San Diego Regional Energy Innovation Network Info Session",
    date = "2019-1-31",
    time = "11:30",
    company = company21,
    location = " The Basement - Mandeville B202",
    type = 0,
    description = "Come learn about the San Diego Regional Energy Innovation Network (SDREIN) program, led by Cleantech San Diego and supported by 8 partner organizations (including UC San Diego) that offers free services to help clean energy startups commercialize their technologies. This info session will feature a 20 min presentation and plenty of time for Q&A. Hear about how your business can benefit, what it takes to apply and be accepted, and what successes current and past program members have experienced from being involved.   ABOUT SDREIN:  The San Diego Regional Energy Innovation Network is a free program for startups that are developing solutions to help California meet its energy goals. The program is funded through a grant from the California Energy Commission and provides access to the resources and facilities of a number of regional partner organizations and connections with industry in order to accelerate the commercialization of emerging energy technologies.",
    num_views = 1023,
    num_favorites=678)
event12.save()

event13=Event.objects.create(
    event_name="Master's and PhD Career Development Week",
    date = "2019-3-25",
    time = "8:00",
    company = company21,
    location = "9500 Gilman Dr, La Jolla, California 92093, United States",
    type = 1,
    description = "Want to network with employers? Interested in mock interviewing with a real hiring manager? Need to learn from your peers who recently made the jump from academia to industry? Then the Master's and PhD Career Development Week is just for you!   Developed exclusively to serve the needs of graduate students and postdoctoral scholars, the specialized workshops, panels and mixers will provide you with the tools and information you'll need to succeed. Look for more event and registration details in the coming months.",
    num_views = 849,
    num_favorites=685)
event13.save()

event14=Event.objects.create(
    event_name="2019 Triton Winter Career Fair",
    date = "2019-1-16",
    time = "10:00",
    company = company21,
    location = "UC San Diego Price Center 9500 Gilman Drive, La Jolla, CA 92093, United States Favorite",
    type = 0,
    description = "It's never too early (or late) to explore career opportunities! The Career Center's Industry Engagement Team works with leading employers from every industry to bring internship and job opportunities to students and alumni through Career Fairs. Attend UC San Diego Career Fairs where you can meet with employers face-to-face. We anticipate 7+employers! Reserve your spot today!",
    num_views = 34982,
    num_favorites=27832)
event14.save()

event15=Event.objects.create(
    event_name="National Collegiate Virtual Career Fair",
    date = "2019-3-21",
    time = "10:00",
    company = company21,
    location = "Virtual career fair from your location",
    type = 1,
    description = "NATIONAL COLLEGIATE VIRTUAL CAREER FAIR March 21, 2019 | 10:00AM - 7:00PM EST | Join this Live Online Event!",
    num_views = 789,
    num_favorites=746)
event15.save()

event16=Event.objects.create(
    event_name="UCSD's 2018 Hackathon",
    date = "2018-11-26",
    time = "8:00",
    company = company21,
    location = "UCSD",
    type = 1,
    description = "lan Turing Memorial Scholarship Winners - Techniques that Expose Your Browsing History to Attackers - Three New CSE Faculty Members - $10 Million Grant for Center for Trustworthy Machine Learning - Health, Homecare and Robotics - $2 Million Grant for Research Program for Underrepresented Groups - 2019 CSE Research Open House",
    num_views = 453,
    num_favorites=425)
event16.save()

event17=Event.objects.create(
    event_name="CSE Alumnus's Startup Shows Tech Takeovers Can Happen... Even in Smaller Markets",
    date = "2018-1-17",
    time = "7:30",
    company = company21,
    location = "UCSD",
    type = 0,
    description = "Just because he's not in Silicon Valley or San Diego doesn't mean that CSE alumnus Matthew Der (M.S., Ph.D. '13, '15) couldn't work for a dynamic startup that would attract a blue-chip takeover. That's exactly what happened to Notch, Co., a tech consulting firm in his hometown of Richmond, Virginia. A year after CEO Paul Hurlocker and Der's brother David started the company in 2014, Matt Der joined as Chief Technology Officer in 2015 after completing his Ph.D. in Computer Science at UC San Diego, with a focus on machine learning. His dissertation involved Investigating Large-Scale Internet Abuse through Web Page Classification.",
    num_views = 474,
    num_favorites=464)
event17.save()

event18=Event.objects.create(
    event_name="Strong CSE Presence at Top Machine Learning Conference",
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
    event_name="33A Introduction to Composition",
    date = "2018-12-5",
    time = "14:00",
    company = company21,
    location = "Recital Hall, Conrad Prebys Music Center",
    type = 0,
    description = "Program information to be announced.",
    num_views = 433,
    num_favorites=425)
event19.save()


event20=Event.objects.create(
    event_name="ECE115 Fast Prototyping: Final Project Open House",
    date = "2018-3-15",
    time = "15:00",
    company = company21,
    location = "Jacobs School of Engineering Lobby, 9500 Gilman Dr, La Jolla, San Diego, California 92093",
    type = 1,
    description = "This design-focused course pairs students into groups of two, and teaches them how to prototype a mechatronic solution as quickly as possible. Students gain hands-on skills and experience with design, fabrication, integration, and characterization of practical electronic and mechanical hardware systems. Students learn to materialize their ideas in the shortest possible time and make design decisions that will result in a cost-effective, robust, and well-designed mechatronic system.",
    num_views = 637,
    num_favorites=476)
event20.save()


event21=Event.objects.create(
    event_name="MBA Program Overview and Admissions Q&A Webinar",
    date = "2018-12-12",
    time = "17:30",
    company = company21,
    location = "Rady School of Management, 9500 Gilman Dr, La Jolla, CA 92093",
    type = 0,
    description = "Join the MBA Sr. Assistant Directors for a virtual information session on the MBA full time and part time programs. You will learn application tips and insight on how to create a competitive application with Admissions Q & A time.",
    num_views = 984,
    num_favorites=869)
event21.save()

event22=Event.objects.create(
    event_name="Inside the MBA - San Francisco",
    date = "2019-1-23",
    time = "18:30",
    company = company21,
    location = "780 Mission St, San Francisco, CA 94103",
    type = 1,
    description = "This event will provide an opportunity for prospective MBA students to gain insights about business school, including how to choose an MBA program and navigate the MBA admissions process. Space is limited so please register early!",
    num_views = 794,
    num_favorites=453)
event22.save()

event23=Event.objects.create(
    event_name="Inside the MBA - Los Angeles",
    date = "2019-1-24",
    time = "18:30",
    company = company21,
    location = "This event will provide an opportunity for prospective MBA students to gain insights about business school, including how to choose an MBA program and navigate the MBA admissions process. Space is limited so please register early!",
    type = 0,
    description = "Meet some employees from facebooks and get chance to hand in resume!",
    num_views = 756,
    num_favorites=671)
event23.save()

event24=Event.objects.create(
    event_name="Rady Live: Master of Science in Business Analytics Application Tips Webinar",
    date = "2018-11-27",
    time = "17:00",
    company = company21,
    location = "Rady School of Management, 9500 Gilman Dr, La Jolla, CA 92093",
    type = 1,
    description = "Join MSBA admissions advisor, Emily Dayton for a virtual information session program on the MSBA application process, with Q&A, application tips and tricks, and insight on how to be a strong applicant to this competitive program.",
    num_views = 483,
    num_favorites=912)
event24.save()

event25=Event.objects.create(
    event_name="Coffee and Conversation with Rady Admissions",
    date = "2018-11-14",
    time = "8:00",
    company = company21,
    location = "Green Acre Campus Pointe 10300 Campus Point Dr, San Diego, CA 92121",
    type = 0,
    description = "Take time out for a coffee break and learn how you can advance your career with a specialized Master's in Business Analytics, Finance or Accountancy from the Rady School School of Management. Meet with an Admissions Advisor from the Rady School and find out why Rady has the curriculum, the network, and the impact you need to make changes happen in your career.",
    num_views = 347,
    num_favorites=265)
event25.save()

event26=Event.objects.create(
    event_name="UCSD Extension GMAT & GRE Prep",
    date = "2018-11-6",
    time = "10:00",
    company = company21,
    location = "6256 Greenwich Dr, San Diego, CA 92122",
    type = 1,
    description = "Meet Rady at the UC San Diego Extension campus! A representative from the Rady School of Management will be answering questions regarding the GRE, providing test-prep information, and much more.",
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
    event_name="Graduate Admissions Events Schedule",
    date = "2018-11-7",
    time = "11:00",
    company = company21,
    location = "CSUB Stockdale Hwy, Bakersfield, CA 93311",
    type = 1,
    description = "Join us at the Cal State Bakersfield Graduate School Fair! Here, you will be able to speak with a representative from the Rady School of Management and have your admissions questions answered, receive GMAT test-prep advice, and much more.",
    num_views = 632,
    num_favorites=589)
event28.save()

event29=Event.objects.create(
    event_name="Master of Finance Info Session Webinar",
    date = "2018-11-15",
    time = "16:00",
    company = company21,
    location = "Rady School of Management, 9500 Gilman Dr, La Jolla, CA 92093",
    type = 0,
    description = "Join us for a virtual information session program overview, Q&A with the Masters of Finance admissions adviser, and hear from Masters of Finance Faculty, Professor Michael Melvin on how this program prepares graduates to tackle significant challenges facing the financial sector.",
    num_views = 18273,
    num_favorites=12637)
event29.save()

event30=Event.objects.create(
    event_name="Specialized Master's Brunch",
    date = "2018-11-17",
    time = "10:00",
    company = company21,
    location = "Waypoint Public 3794 30th St, San Diego, CA 92104",
    type = 1,
    description = "Join us for an in-person information session about specialized Master's programs. Hear from the admissions team about the Master of Finance, Master of Professional Accountancy, Master of Business Analytics and what Rady is looking for in its applicants.",
    num_views = 102385,
    num_favorites=93872)
event30.save()

event31=Event.objects.create(
    event_name="MFin Master Class",
    date = "2018-11-28",
    time = "17:00",
    company = company21,
    location = "Rady School of Management Otterson Hall, 3rd Floor (Room 3E107)",
    type = 0,
    description = "Join us for the Rady Finance Master Class with MFin Faculty, Professor Michael Melvin to discuss the lessons learned from the financial crisis and the future of global investing! Meet with faculty and current students in the Master of Finance program to find out how the program, curriculum, and network prepares students to make a significant impact on the financial sector.",
    num_views = 3487,
    num_favorites=2913)

event31.save()

event32=Event.objects.create(
    event_name="Open Data Science Conference - San Francisco",
    date = "2018-10-31",
    time = "9:00",
    company = company21,
    location = "1333 Old Bayshore Hwy, Burlingame, CA 94010",
    type = 0,
    description = "ODSC West 2018 is one of the largest applied data science conferences in the world. Speakers include some of the core contributors to many open source tools, libraries, and languages. Come and learn about the latest AI & data science topics, tools, and languages from some of the best and brightest minds in the field.",
    num_views = 3847,
    num_favorites=3103)
event32.save()


event33=Event.objects.create(
    event_name="Brunch With Rady Admissions (South County)",
    date = "2018-4-28",
    time = "11:00",
    company = company21,
    location = "Waypoint Public 3794 30th St San Diego, CA 92104",
    type = 0,
    description = "Try to learn how to study fast! And share the tips with others!",
    num_views = 3487,
    num_favorites=2913)
event33.save()


event34=Event.objects.create(
    event_name="Rady's Womens Forum",
    date = "2018-4-21",
    time = "11:00",
    company = company21,
    location = "UC San Diego Rady School of Management - Otterson Hall, Multi Purpose Room 2, 2S117 La Jolla, CA 92093",
    type = 1,
    description = "RADY'S WOMENS FORUM - DISCUSSION AND ACTION PLAN FOR VIBRANT LEADERS This special event is designed specifically for women and will include presentations, workshops and discussions by distinguished Rady women and alumnae. Topics will include effective negotiations, navigating male dominated environments, creating your personal brand and career enhancing tips and strategies.Lunch will be included and an afternoon dessert reception will sure to expand you women's network. Come learn from our vibrant Rady Women leaders.",
    num_views = 3328,
    num_favorites=1845)
event34.save()


event35=Event.objects.create(
    event_name="Scientists & Engineering at Rady - Special Event",
    date = "2018-4-10",
    time = "17:30",
    company = company21,
    location = "UC San Diego, Rady School of Management Otterson Hall - Sky Pavilion, 5th floor",
    type = 0,
    description = "The Rady School of Management Graduate Admissions is hosting a special event for individuals with a background in science or engineering.  Join us as we discuss why you should consider a business degree and how it can complement your science or engineering background. The program will consist of a light dinner, a presentation, and a panel of Rady students and alumni as they discuss how they have added value to their science or engineering backgrounds with a business degree from the Rady School of Management. They will share insights and career strategies for networking, leadership, and innovation.",
    num_views = 1392,
    num_favorites=1647)
event35.save()


event36=Event.objects.create(
    event_name="Breakfast and Conversation with Rady Admissions (La Jolla)",
    date = "2018-2-22",
    time = "8:00",
    company = company21,
    location = "Green Acre Campus Pointe 10300 Campus Point Dr, San Diego, CA 92121",
    type = 1,
    description = "Join us for breakfast and learn how you can advance your career with a FLEX part time MBA from the Rady School School of Management. Meet with admissions staff from the Rady School and find out why Rady has the curriculum, the network, and the impact you need to make changes happen in your career.",
    num_views = 7634,
    num_favorites=6734)
event36.save()


event37=Event.objects.create(
    event_name="Breakfast and Conversation with Rady Admissions (Liberty Station)",
    date = "2018-2-27",
    time = "8:00",
    company = company21,
    location = "Join us for breakfast and learn how you can advance your career with a FLEX part time MBA from the Rady School School of Management. Meet with the Director from the Rady School and find out why Rady has the curriculum, the network, and the impact you need to make changes happen in your career.",
    type = 0,
    description = "Learn how engineering in Disney support the team and change the world!",
    num_views = 5285,
    num_favorites=4828)
event37.save()

event38=Event.objects.create(
    event_name="Rady[X] Tech Conference",
    date = "2018-3-2",
    time = "11:00",
    company = company21,
    location = "Rady School of Management",
    type = 1,
    description = "The Rady Technology Club presents its fourth annual technology conference. The day will consist of keynote presentations, a tech fair featuring local businesses and startups, company presentations, a Q&A session and a catered networking mixer. Don't miss this chance to get up close and personal with leaders from the some of the most innovative companies and startups!",
    num_views = 4983,
    num_favorites=4562)
event38.save()

event39 =Event.objects.create(
    event_name="Preview Day - Campus Visit Day Spring 2018",
    date = "2018-3-3",
    time = "9:00",
    company = company21,
    location = "Rady School of Management Wells Fargo Hall,La Jolla, CA 92093",
    type = 0,
    description = "Visit the Rady School of Management and become part of our innovative business environment firsthand during our upcoming Rady Preview Day. This is the best opportunity to see what makes Rady stand out from other schools: our students, our staff, our faculty...our community. We will bring together representatives from all parts of our Rady community to experience what life will be like for you, as a candidate, in one of our Master's programs.",
    num_views = 3726,
    num_favorites=3469)
event39.save()

event40 =Event.objects.create(
    event_name="Rady Live: Master of Finance Virtual Info Session",
    date = "2018-2-28",
    time = "16:00",
    company = company21,
    location = "https://register.gotowebinar.com/register/1472916060966832641",
    type = 1,
    description = "Interested in our Rady Master of Finance Program, but have not had an opportunity to stop by the Rady School of Management for an in person visit?Join us for a virtual information session program overview,  Q&A with the MFIN admissions advisor, and hear from MFIN Faculty, Professor Michael Melvin on how this program prepares graduates to tackle significant challenges facing the financial sector.",
    num_views = 3562,
    num_favorites=2761
)
event40.save()

event61=Event.objects.create(
    event_name="Coffee and Conversation with Rady Admissions (UTC)",
    date = "2018-5-9",
    time = "8:00",
    company = company21,
    location = "Green Arce Campus Pointe 10300 Campus Point Dr, San Diego, CA 92121",
    type = 1,
    description = "Take time out for a coffee break and learn how you can advance your career with an Admissions Advisor from the Rady School and find out why Rady has the curriculum, the network, and the impact you need to make changes happen in your career.",
    num_views = 1230,
    num_favorites=539)
event61.save()

event62=Event.objects.create(
    event_name="Brunch with Rady Admissions (Pacific Beach)",
    date = "2018-6-13",
    time = "8:00",
    company = company21,
    location = "Fig Tree Cafe 5119 Cass St, San Diego, CA 92109",
    type = 1,
    description = "Take time out for a coffee break and learn how you can advance your career with an MBA from the Rady School of Management. Meet with an Admissions Advisor from the Rady School and find out why Rady has the curriculum, the network, and the impact you need to make changes happen in your career.",
    num_views = 3321,
    num_favorites=655)
event62.save()

event63=Event.objects.create(
    event_name="The MBA Tour - LA",
    date = "2018-7-14",
    time = "11:30",
    company = company21,
    location = "LA Hotel Downtown (soon to be Hyatt Regency) 333 South Figueroa Street Los Angeles, CA 90071 USA",
    type = 0,
    description = "Meet face-to-face with the MBA admissions officers and alumni of the world’s top business schools, as well as attend GMAT and admissions strategy workshops on building a winning MBA applications, and more",
    num_views = 3392,
    num_favorites=123)
event63.save()

event64=Event.objects.create(
    event_name="Rady Golf Classic",
    date = "2018-8-27",
    time = "11:30",
    company = company21,
    location = "La Jolla Country Club 7301 High Ave, San Diego, CA 92037",
    type = 1,
    description = "Join the Rady School of Management for a great day of golf to support fellowships for MBA students. Mingle with innovations and network with prominent community leaders at the exclusive La Jolla Country Club ",
    num_views = 10,
    num_favorites=0)
event64.save()

event65=Event.objects.create(
    event_name="Pepperdine University - Business School Fair",
    date = "2018-9-10",
    time = "17:00",
    company = company21,
    location = "24255 Pacific Coast Highway, Malibu, CA, 90263",
    type = 1,
    description = "Meet the Rady at the Business Career Fair hosted by Pepperdine University in Malibu, CA. You will be able to speak with a representative from the Rady School of Management and have your admissions, GMAT, GRE, and many more questions answered.",
    num_views = 3344,
    num_favorites=1111)
event65.save()

event66=Event.objects.create(
    event_name="QS Masters Connect - NYC",
    date = "2018-9-15",
    time = "10:00",
    company = company21,
    location = "1335 6th Ave, New York, NY 10019",
    type = 0,
    description = "Meet the Rady of Management at the QS Connect Masters fair in New York City! You will be able to speak with a representative from the Rady School of Management and have your admissions, GMAT, GRE, and many more questions answered. Space is limited so please register today!",
    num_views = 1890,
    num_favorites=13)
event66.save()

event67=Event.objects.create(
    event_name="Pepperdine University - Business School Fair",
    date = "2018-9-25",
    time = "10:00",
    company = company21,
    location = "Logan, UT 84322",
    type = 0,
    description = "Meet the Rady at Utah State University! You will be able to speak with a representative from the Rady School of Management and have your admissions, GMAT, GRE, and many more questions answered.",
    num_views = 666,
    num_favorites=21)
event67.save()

event68=Event.objects.create(
    event_name="Inside the MBA",
    date = "2018-9-24",
    time = "18:30",
    company = company21,
    location = "400 West Broadway, San Diego, CA 92101",
    type = 1,
    description = "This event will provide an opportunity for prospective MBA students to gain insights about business school, including how to choose an MBA program and navigate the MBA admissions process. Space is limited so please register early!",
    num_views = 3344,
    num_favorites=1111)
event68.save()

event69=Event.objects.create(
    event_name="Weber State University",
    date = "2018-9-26",
    time = "10:30",
    company = company21,
    location = "3848 Harrison Blvd, Ogden, UT 84408",
    type = 0,
    description = "Meet Rady at Weber State University! You will be able to speak with a representative from the Rady School of Management and have your admissions, GMAT, GRE, and many more questions answered.",
    num_views = 1233,
    num_favorites=46)
event69.save()

event70=Event.objects.create(
    event_name="QS Masters Connect - San Francisco",
    date = "2018-9-22",
    time = "13:00",
    company = company21,
    location = "5 Embarcadero Center, San Francisco, CA 94111",
    type = 1,
    description = "Join us at the largest MBA Tour in San Francisco! You will be able to speak with a representative from the Rady School of Management and have your admissions, GMAT, GRE, and many more questions answered. Space is limited so please register today!",
    num_views = 689,
    num_favorites=99)
event70.save()

event71=Event.objects.create(
    event_name="University of Utah/Westminster",
    date = "2018-9-27",
    time = "10:00",
    company = company21,
    location = "201 Presidents Cir, Salt Lake City, UT 84112",
    type = 0,
    description = "Meet Rady at the University of Utah/Westminster! You will be able to speak with a representative from the Rady School of Management and have your admissions, GMAT, GRE, and many more questions answered. Space is limited so please register today!",
    num_views = 937,
    num_favorites=112)
event71.save()

event72=Event.objects.create(
    event_name="Northern Arizona University",
    date = "2018-9-28",
    time = "12:00",
    company = company21,
    location = "S. San Francisco St, Flagstaff, AZ 86011",
    type = 1,
    description = "Meet Rady at the Northern Arizona University! You will be able to speak with a representative from the Rady School of Management and have your admissions, GMAT, GRE, and many more questions answered. Space is limited so please register today!",
    num_views = 666,
    num_favorites=26)
event72.save()

event73=Event.objects.create(
    event_name="Effective Business Writing",
    date = "2018-12-7",
    time = "8:30",
    company = company21,
    location = "Training Center North (Plaza Level, Torrey Pines Center-North)",
    type = 0,
    description = "Learn effective business writing techniques during this interactive, content-rich and engaging class",
    num_views = 245,
    num_favorites=12)
event73.save()

event74=Event.objects.create(
    event_name="Learning Protein Dynamics from Data",
    date = "2018-11-13",
    time = "11:00",
    company = company21,
    location = "AP&M 2402",
    type = 0,
    description = "Biological data sets, such as gene expressions or protein levels, are often high-dimensional, and thus difficult to interpret. Finding important structural features and identifying clusters in an unbiased fashion is a core issue for understanding biological phenomena.",
    num_views = 69,
    num_favorites=0)
event74.save()

event75=Event.objects.create(
    event_name="Learning Protein Dynamics from Data",
    date = "2018-12-14",
    time = "11:00",
    company = company21,
    location = "AP&M 2402",
    type = 0,
    description = "Nowadays, data is exploding at a faster rate than computer architectures can handle. For that reason, mathematical techniques to analyze large-scale data need be developed. Stochastic iterative algorithms have gained interest due to their low memory footprint and adaptability for large-scale data. In this talk, we will present the Randomized Kaczmarz algorithm for solving extremely large linear systems of the form Ax=y.",
    num_views = 135,
    num_favorites=5)
event75.save()

event76=Event.objects.create(
    event_name="Connect MBA - NYC",
    date = "2018-11-17",
    time = "16:00",
    company = company21,
    location = "270 W 43rd St, New York, NY 10036",
    type = 0,
    description = "Join us at New York's largest networking event! Here, you will be able to speak with a representative from the Rady School of Management and have your admissions questions answered, receive GMAT test-prep advice, and much more.",
    num_views = 1350,
    num_favorites=109)
event76.save()

event77=Event.objects.create(
    event_name="QS MBA - Denver",
    date = "2018-10-23",
    time = "16:30",
    company = company21,
    location = "1405 Curtis Street, Denver, CO 80202",
    type = 1,
    description = "Join us at the largest MBA Tour in Denver! Here, you will be able to speak with a representative from the Rady School of Management and have your admissions questions answered, receive GMAT test-prep advice, and much more.",
    num_views = 3125,
    num_favorites=269)
event77.save()

event78=Event.objects.create(
    event_name="Meet the Firms (MPAc)",
    date = "2018-10-11",
    time = "17:0",
    company = company21,
    location = "Price Center, La Jolla, CA 92093",
    type = 1,
    description = "Join us for UC San Diego's Annual Meet The Firms Accounting Fair. Hosted by UC San Diego's Career Center, Alumni, Rady School of Management, Department of Economics, and Undergraduate Accounting Society, this event is the premier networking event of the accounting recruiting season.",
    num_views = 1260,
    num_favorites=133)
event78.save()

event79=Event.objects.create(
    event_name="Rady Student Alumni Panel",
    date = "2018-10-24",
    time = "17:30",
    company = company21,
    location = "9500 Gilman Drive Otterson Hall - MPR2 (2S117) La Jolla, CA 92093",
    type = 0,
    description = "This event will have an alumni student experience focus and will inform prospective students how getting a Rady degree will help with their professional advancement. Light food will be served. This is a free event, however registration is requested for planning purposes.",
    num_views = 3125,
    num_favorites=269)
event79.save()

event80=Event.objects.create(
    event_name="Data Science Go Conference",
    date = "2018-10-12",
    time = "16:00",
    company = company21,
    location = "4240 La Jolla Village Dr, La Jolla, CA 92037",
    type = 0,
    description = "Join us at DataScienceGO; the only conference dedicated to career advancement for data science practitioners and beginners. DSGO is three days of immersive talks, panels, and training sessions designed to teach, inspire, and guide you. Space is limited so make sure to register early!",
    num_views = 666,
    num_favorites=1)
event80.save()