from django.contrib import admin

# Register your models here.
from User.models import User, Major, Degree, Request
admin.site.register(User)
admin.site.register(Major)
admin.site.register(Degree)
admin.site.register(Request)
