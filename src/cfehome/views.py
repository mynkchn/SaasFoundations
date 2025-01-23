from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from visits.models import PageVisit
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.conf import settings

LOGIN_URL=settings.LOGIN_URL

def home_page_view(request,*args, **kwargs) :

      qs=PageVisit.objects.all()
      page_visits=PageVisit.objects.filter(path=request.path)

      context={
            
            'pagevisit_count':page_visits.count(),
            'total_count':qs.count(),
            'percent':(page_visits.count()*100.0)/  qs.count() if qs.count() > 0 else 0,
      }
      if not page_visits.exists():
        PageVisit.objects.create(path=request.path)

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