from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    meetups=[
        {'title':'A First Meetup'},{'title':' A Second Meetup'}
    ]
    return render(request,"meetups/index.html",{'meetups':meetups,'show_meetups':False})
