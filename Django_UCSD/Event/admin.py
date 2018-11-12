from django.contrib import admin

# Register your models here.
from Event.models import Event

admin.site.register(Event)