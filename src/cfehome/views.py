from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from visits.models import PageVisit



def home_page_view(request,*args, **kwargs) :

      qs=PageVisit.objects.all()
      page_visits=PageVisit.objects.filter(path=request.path)

      context={
            
            'pagevisit_count':page_visits.count(),
            'total_count':qs.count(),
            'percent':(page_visits.count()*100.0)/qs.count(),
      }
      PageVisit.objects.create(path=request.path)

      return render(request,'home.html',context)
