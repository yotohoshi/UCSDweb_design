from django.db import models
import Company.models
import django.core.validators
import uuid
from datetime import date, datetime, timedelta


# Create your models here.
# Global Variables
TODAY = date.today()
NOW = datetime.now()


class Event(models.Model):
    event_id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    event_name = models.CharField(max_length=150)
    date = models.DateField(auto_now=False, auto_created=False, auto_now_add=False)
    time = models.TimeField(auto_now=False, auto_created=False, auto_now_add=False)
    company = models.ForeignKey(Company.models.Company, on_delete=models.PROTECT)
    location = models.CharField(max_length=100)
    type = models.IntegerField(
        validators=[django.core.validators.MaxValueValidator(1), django.core.validators.MinValueValidator(0)])
    description = models.CharField(max_length=1000, default="This event have no descriptions yet.")
    num_views = models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])
    num_favorites = models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])

    # category = models.IntegerField(max_length=2, null=False),
    # Getters
    @staticmethod
    def get_event_by_company(company):
        if type(company) != Company.models.Company:
            return
        else:
            return list(Event.objects.filter(company=company))

    # TODO Filter Functions
    @staticmethod
    def all_filter_by_today():
        toReturn = list(Event.objects.filter(date=TODAY))
        return toReturn

    @staticmethod
    def all_filter_by_month():
        all_events = list(Event.objects.all())
        toReturn = list()
        for i in all_events:
            if i.date.year == TODAY.year and i.date.month == TODAY.month:
                toReturn.append(i)
        return toReturn

    @staticmethod
    def all_filter_by_week():
        start_week = TODAY - timedelta(TODAY.weekday())
        end_week = start_week + timedelta(7)
        toReturn = list(Event.objects.filter(date__range=[start_week, end_week]))
        return toReturn

    @staticmethod
    def get_top_five():
        all_events = list(Event.objects.all())
        all_events.sort(key=Event.rank, reverse=True)
        toReturn = list()
        count = 0
        while count < 5:
            toReturn.append(all_events[count])
            count += 1
        return toReturn

    # Other functions
    def rank(self):
        return int(self.num_favorites * 10 + self.num_views)

    def update_num_favorite(self):
        self.num_favorites = self.user_set.all().count()
        return

    def increment_num_views(self):
        self.num_views += 1
        return

    def __str__(self):
        return self.event_name+str(self.time)+self.company.company_name

    def set_event_name(self, name):
        if type(name) != str:
            return False
        else:
            self.event_name = name
            return True

    def set_date(self, Edate):
        if type(Edate) != date:
            return False
        else:
            self.date = Edate

    def set_company(self, company):
        if type(company) != Company.models.Company:
            return False
        else:
            self.company = company
            return True

    def set_location(self, loc):
        if type(loc) != str:
            return False
        else:
            self.location = loc
            return True

    def set_event_type(self, tp):
        if type(tp) != int or tp < 0 or tp > 1:
            return False
        else:
            self.type = tp
            return True

    def set_description(self, descrip):
        if type(descrip) != str or len(descrip) > 1000:
            return False
        else:
            self.description = descrip
            return True




