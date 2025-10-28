from django.http import HttpResponse,HttpResponseRedirect,HttpResponseNotFound
from django.urls import reverse
from django.shortcuts import render 
from django.template.loader import render_to_string

def january(request):
    return HttpResponse("This is the beginning of an year")

def february(request):
    return HttpResponse("Walk for atleast 20 minutes a day!")

monthly_challenges ={
     "january":"This is a very new beginning",
     "february":"Walk 20 mins every day",
     "march":"Learn Django for 20 mins a day",
     "april":"Reduce eating red meat",
     "may":"Pray for 15 minutes a day",
     "june":"Join a Gym",
     "july":"Participate in charity ",
     "august":"Take a whole body checkup",
     "september":"Reduce your screen time",
     "october":"Go for trekking",
     "november":"Learn a programming language",
     "december":"Sleep on Time"
 }

#Sleep on Time

def monthly_challenge(request, month):
	try:
		challenge_text=monthly_challenges[month]
		return render(request,"challenges/challenge.html",{"text":challenge_text,"month":month})
	except:
		challenge_text=f"<h1>Month is Invalid !!!</h1>"
		return HttpResponseNotFound(challenge_text)


def index(request):
	months=list(monthly_challenges.keys())
	return render(request,"challenges/index.html",{"months":months})

def monthly_challenge_by_month(request,month):
	if(month<=0 or month>12):
		return HttpResponse("The month is invalid")
	else:
		months=list(monthly_challenges.keys())
		redirected_month=months[month-1]
		redirected_url=reverse("monthly_challenge",args=[redirected_month])
		return HttpResponseRedirect(redirected_url)











	# if month == "january":
	# 	challenge_text = "Embrce new beginnings"
	# elif month == "march":
	# 	challenge_text = "Reduce the Consumption of Red Meat"
	# elif month == "february":
	# 	challenge_text = "Walk for atleast 20 minutes a day!"
	# else:
	# 	challenge_text = None
	# return challenge_text
	
	
		
        