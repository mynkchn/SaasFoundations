from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages



def home_page_view(request,*args, **kwargs) :
      return HttpResponse("Welcome to my home page")