from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404

User=get_user_model()
# Create your views here.
@login_required
def profile_view(request,username=None,*args, **kwargs) :
    # <app_label>.view_model_name>
    # <app_label>.delete_model_name>
    # <app_label>.add_model_name>
    user=request.user
    permission=user.has_perm("auth.view_user")
    bool=False
    profile_user_obj=get_object_or_404(User,username=username)
    if user.username==profile_user_obj.username:
        bool=True
    if user.has_prem("visits.view_pagevisit") :
        pass
        # qs=Pagevisit.objects.all()
    return HttpResponse(f"Hey wassup {username} - {profile_user_obj.id} {bool} does have premission -{permission}")