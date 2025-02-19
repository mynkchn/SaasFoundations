from django.contrib import admin
from .models import Subscriptions,UserSubscription
# Register your models here.
admin.site.register(Subscriptions)
admin.site.register(UserSubscription)