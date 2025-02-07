from django.core.management import BaseCommand
from typing import Any
from subscriptions.models import Subscriptions

class Command(BaseCommand) :
    def handle(self,*args:Any,**options:Any) :
        qs=Subscriptions.objects.filter(active=True)
        for obj in qs:
            print(qs) 
            for group in obj.groups.all():
                print(group)
                for per in obj.permissions.all() :
                    print(per)
                    group.permissions.add(per)
