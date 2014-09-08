from django.shortcuts import render_to_response
import datetime
from models import People

def index(request):
    now=datetime.datetime.now()
    return render_to_response('index.html',{'blogs':now})

def about(request):
    return render_to_response('about.html',{})

def blogList(request):
    return render_to_response('blog/bloglist.html',{})
