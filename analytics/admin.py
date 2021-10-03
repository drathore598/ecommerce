from django.contrib import admin

from analytics.models import ObjectViewed, UserSession

# Register your models here.
admin.site.register(ObjectViewed)

admin.site.register(UserSession)