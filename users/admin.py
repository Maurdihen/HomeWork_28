from django.contrib import admin

from users.models import User, Location

admin.site.register(User)
admin.site.register(Location)
