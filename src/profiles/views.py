from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.conf import settings
User=get_user_model()
LOGIN_URL=settings.LOGIN_URL
# Create your views here.

@login_required
def profile_list_view(request,*args,**kwargs) :
    context={
        'objects_list': User.objects.filter(is_active=True)
    }
    

    return render(request,'profiles/list.html',context)


@login_required
def profile_detail_view(request,username=None,*args,**kwargs) :
    user=request.user
    if user.has_perm('subscription.basic') :
        return HttpResponse("Basic Subscription")
    # <app_label>.view_model_name>
    # <app_label>.delete_model_name>
    # <app_label>.add_model_name>
   
    permission=user.has_perm("auth.view_user") or False
    bool=False
    profile_user_obj=get_object_or_404(User,username=username)
    if user.username==profile_user_obj.username:
        bool=True
        permission=user.has_perm("auth.view_user") or False
    if user.has_perm("visits.view_pagevisit") :
        pass
    context ={
        'opener':bool,
        'permission':permission,
        'object':profile_user_obj,
        'instance':user,

    }
        # qs=Pagevisit.objects.all()
    return render(request,'profiles/detail.html',context)