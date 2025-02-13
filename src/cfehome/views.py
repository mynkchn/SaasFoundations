from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib import messages
from visits.models import PageVisit
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.conf import settings
import requests
from .utils import get_response
from django.http import JsonResponse

LOGIN_URL=settings.LOGIN_URL
# NASA_API_KEY=getattr(settings,'NASA_API_KEY')

def home_page_view(request,*args, **kwargs) :
      qs=PageVisit.objects.all()
      pagevisit_add=PageVisit.objects.create(path=request.path)
      pagevisit=PageVisit.objects.filter(path=request.path)
      
      context={
         'total_page_count':qs.count(),
         'page_visit_count':pagevisit.count(),

      }
      if request.method=='POST' :
         response=request.POST['response']
         answer=get_response(response)
         return JsonResponse(answer)
      

      return render(request,'home.html',context)

VALID_CODE='abc123'
def pw_protected_view(request,*args,**kwargs) :
    is_allowed=request.session.get('protected_page_allowed') or 0
    # print(request.session.get('protected_page_allowed'),type(request.session.get('protected_page_allowed')) )
    if request.method=='POST':
     user_pw_sent=request.POST['code'] or None
     if user_pw_sent==VALID_CODE :
        is_allowed=1
        request.session['protected_page_allowed']=is_allowed

    if is_allowed :
       return render(request,'protected/view.html')
    return render(request,'protected/entry.html')

@login_required(login_url=LOGIN_URL)
def user_only_view(request,*args,**kwargs) :

     return render(request,'protected/user-only.html',{})

@staff_member_required(login_url=LOGIN_URL)
def staff_only_view(request,*args,**kwargs) :
   
   return render(request,'protected/user-only.html',{})


        

