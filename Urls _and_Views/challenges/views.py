from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

def january(request):
    return HttpResponse("This is the beginning of an year")

def february(request):
    return HttpResponse("Walk for atleast 20 minutes a day!")

monthly_challenges = {
    "january": "Eat no meat for the entire month!",
    "february": "Walk for at least 20 minutes every day!",
    "march": "Learn Django for at least 20 minutes every day!",
    "april": "Eat no meat for the entire month!",
    "may": "Walk for at least 20 minutes every day!",
    "june": "Learn Django for at least 20 minutes every day!",
    "july": "Eat no meat for the entire month!",
    "august": "Walk for at least 20 minutes every day!",
    "september": "Learn Django for at least 20 minutes every day!",
    "october": "Eat no meat for the entire month!",
    "november": "Walk for at least 20 minutes every day!",
    "december": "Learn Django for at least 20 minutes every day!"
}


def monthly_challenge(request, month):
	challenge_text = None
	if month == "january":
		challenge_text = "Embrce new beginnings"
	elif month == "march":
		challenge_text = "Reduce the Consumption of Red Meat"
	elif month == "february":
		challenge_text = "Walk for atleast 20 minutes a day!"
	else:
		challenge_text = "Invalid Month!"
	return HttpResponse(challenge_text)


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
	
	
		
        