from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages



def home_page_view(request,*args, **kwargs) :
      return render(request,'base.html')