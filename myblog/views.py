from django.shortcuts import render_to_response
from models import People
from django.http import HttpResponse
import datetime

def show_peoplelist(request):
    #people_list = People.objects.order_by('-age')[:10]
    return render_to_response('peoplelist.html', {})

def hello(request):
    now=datetime.datetime.now()
    return HttpResponse("xiaochouchou! i love you!%s" % now)

def plus_time(request,offset):
    now=int('a-')
    return HttpResponse("hello,%s" % offset)
