#coding=utf-8
from django.shortcuts import render_to_response
import datetime
from models import People
from django.db import connection

def index(request):
    now=datetime.datetime.now()
    return render_to_response('index.html',{'blogs':now})

def about(request):
    return render_to_response('about.html',{})

def blogList(request):
    cursor=connection.cursor()

    cursor.execute('select * from test')
    names=cursor.fetchall()
    s=[names[0][1]]
    return render_to_response('blog/bloglist.html',{'blogname':s})

