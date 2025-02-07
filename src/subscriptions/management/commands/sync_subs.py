from django.core.management.base import BaseCommand
from subscriptions.models import Subscriptions
from typing import Any

class Command(BaseCommand):
    def handle(self,*args:Any, **options:Any):
     qs=Subscriptions.objects.filter(active=True)
     print(x[0] for x in qs)
     for obj in qs:
        for group in obj.groups.all() :
           print(group)
           for per in obj.premission.all() :
             print(per)
             group.permissions.add(per)
        
