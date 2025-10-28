from django.urls import path
from . import views

urlpatterns=[
    path("",views.index,name="index"),#Trigger /challenges/
    path("<int:month>/",views.monthly_challenge_by_month),
    path("<str:month>/",views.monthly_challenge,name="monthly_challenge")
]


# urlpatterns=[
#     path("january/",views.january),
#     path("february/",views.february),
#     path("<month>",views.monthly_challenges)   
# ]