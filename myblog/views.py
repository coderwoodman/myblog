from django.shortcuts import render_to_response
from models import People
from django.http import HttpResponse

def show_peoplelist(request):
    #people_list = People.objects.order_by('-age')[:10]
    return render_to_response('peoplelist.html', {})

def hello(request):
	return HttpResponse("xiaochouchou! i love you!")
