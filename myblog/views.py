from django.shortcuts import render_to_response
from models import People
from django.http import HttpResponse
import datetime
from django.template import Template,Context
from django.template.loader import get_template

def show_peoplelist(request):
    #people_list = People.objects.order_by('-age')[:10]
    return render_to_response('peoplelist.html', {})

def hello(request):
    now=datetime.datetime.now()
    t=get_template('test.html')
    html=t.render(Context({'people':now}))
    return HttpResponse(html)

def plus_time(request,offset):
    now=int('a-')
    return HttpResponse("hello,%s" % offset)
