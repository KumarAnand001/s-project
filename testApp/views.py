from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.

def timeInfo(request):

    date = datetime.datetime.now()
    msg = '<h1>Hello Friend Good Evening !!!</h1><hr>'
    msg = msg + '<h1>Now Server time is' + str(date) +'<hr>'

    return HttpResponse(msg)