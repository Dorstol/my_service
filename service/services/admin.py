from django.contrib import admin

from services.models import Service, Plan, Subscription

admin.site.register([Service, Plan, Subscription])
