from django.db import models
import Company.models
import django.core.validators
import uuid


# Create your models here.


class Event(models.Model):
    event_id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    event_name = models.CharField(max_length=100)
    time = models.DateTimeField(auto_now=False, auto_created=False, auto_now_add=False)
    company = models.ForeignKey(Company.models.Company, on_delete=models.PROTECT)
    location = models.CharField(max_length=100)
    type = models.IntegerField(
        validators=[django.core.validators.MaxValueValidator(1), django.core.validators.MinValueValidator(0)])
    description = models.CharField(max_length=300, default="This event have no descriptions yet.")
    num_views = models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])
    num_favorites = models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])
    # category = models.IntegerField(max_length=2, null=False),
    # Getters

    # Other functions
    def update_num_favorite(self):
        self.num_favorites = self.user_set.all().count()
        return
