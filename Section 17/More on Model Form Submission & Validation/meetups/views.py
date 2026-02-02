from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Meetup,Participant
from .forms import RegistrationForm
from django.urls import reverse

def index(request):
    meetups = Meetup.objects.all()
    return render(request,"meetups/index.html",{'meetups':meetups,'show_meetups':True})


def meetup_detail(request,meetup_slug):
    try:
        selected_meetup=Meetup.objects.get(slug=meetup_slug)
        if(request.method=="GET"):
            registration_form=RegistrationForm()
    
        else:
            registration_form=RegistrationForm(request.POST)
            if(registration_form.is_valid()):
                user_email=registration_form.cleaned_data['email']
                participant,_=Participant.objects.get_or_create(email=user_email)
                selected_meetup.participants.add(participant)
                return redirect('confirm_registration',meetup_slug=meetup_slug) 


        return render(request,"meetups/meetup-details.html",{'meetup':selected_meetup,
            'specific_meetup_exist':True,
            'registration_form':registration_form
            })


    
    except Exception as ec :
        return render(request,"meetups/meetup-details.html",{
        'specific_meetup_exist':False
        })
    
def confirm_registration(request,meetup_slug):
    meetup=Meetup.objects.get(slug=meetup_slug)
    organizer_email=meetup.organizer_email
    return render(request,"meetups/registration-success.html",{"organizer_email":organizer_email})



#  return render(request,"meetups/meetup-details.html",{'meetup':selected_meetup,
#             'specific_meetup_exist':True,
#             'registration_form':RegistrationForm
#             })





