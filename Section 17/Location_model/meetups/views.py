from django.shortcuts import render
from django.http import HttpResponse
from .models import Meetup

def index(request):
    meetups = Meetup.objects.all()
    return render(request,"meetups/index.html",{'meetups':meetups,'show_meetups':True})


def meetup_detail(request,meetup_slug):
    try:
        selected_meetup=Meetup.objects.get(slug=meetup_slug)
        return render(request,"meetups/meetup-details.html",{
        'meetup_title':selected_meetup.title,
        'meetup_description':selected_meetup.description,
        'meetup_image':selected_meetup.image,
        'specific_meetup_exist':True
        })
    
    except :
        return render(request,"meetups/meetup-details.html",{
        'specific_meetup_exist':False
        })






