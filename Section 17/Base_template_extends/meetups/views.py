from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    meetups = [
        { 
            'title': 'A First Meetup', 
            'location': 'New York', 
            'slug': 'a-first-meetup' 
        },
        { 
            'title': 'A Second Meetup', 
            'location': 'Paris', 
            'slug': 'a-second-meetup' 
        }
    ]
    return render(request,"meetups/index.html",{'meetups':meetups,'show_meetups':True})


def meetup_detail(request,meetup_slug):
    print(meetup_slug)
    selected_meetup = {
        'title': 'A First Meetup', 
        'description': 'This is the first meetup!'
    }
    return render(request,"meetups/meetup-details.html",{
        'meetup_title':selected_meetup['title'],
        'meetup_description':selected_meetup['description']
    })





