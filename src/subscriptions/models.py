from django.db import models
from django.contrib.auth.models import Group,Permission
from django.conf import settings
from django.db.models.signals import post_save
User=settings.AUTH_USER_MODEL
SUBSCRIPTION_PERMISSION=[
            ('advanced','Advanced Perm'),
            ('pro','Pro Perm'),
            ('basic','Basic Perm'),
            ('basic_ai','Basic_AI Perm'),
     ]

# Create your models here.
ALLOW_CUSTOM_GROUPS=True
class Subscriptions(models.Model) :
    name=models.CharField(max_length=120)
    groups=models.ManyToManyField(Group)
    active=models.BooleanField(default=True)
    permissions=models.ManyToManyField(Permission,
    limit_choices_to={
        'content_type__app_label':'subscriptions',
        'codename__in':[ x[0]for x in SUBSCRIPTION_PERMISSION],
          })
    class Meta:
        permissions=SUBSCRIPTION_PERMISSION
    def __str__(self) :
        return self.name
class UserSubscription(models.Model) :
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    subscriptions=models.ForeignKey(Subscriptions,on_delete=models.SET_NULL,null=True,blank=True)
    active=models.BooleanField(default=True)
def user_sub_post_save(sender,instance,*args, **kwargs):
    user_sub_instance=instance
    user=user_sub_instance.user
    subscription_obj=user_sub_instance.subscriptions
    groups_ids=[]
    if subscription_obj is not None :
 
     groups=subscription_obj.groups.all()
     groups_ids=groups.values_list('id',flat=True)
    if not ALLOW_CUSTOM_GROUPS:
     user.groups.set(groups)
    else :
        sub_qs=Subscriptions.objects.filter(active=True)
        if subscription_obj is not None:
         sub_qs=sub_qs.exclude(id=subscription_obj.id)
        subs_groups=sub_qs.values_list('groups__id',flat=True)
        subs_groups_sets=set(subs_groups)
    
        current_groups=user.groups.all().values_list('id',flat=True)
        groups_ids_set=set(groups_ids)
        current_groups_set=set(current_groups) - subs_groups_sets
        final_group_ids=list(groups_ids_set|current_groups_set)
        user.groups.set(final_group_ids)
post_save.connect(user_sub_post_save,sender=UserSubscription)