from curses.ascii import US
from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Profile
# Create your views here.
def docter_list(request):
    doctors= User.objects.all()
    # doctors= Profile.objects.all()
    print(doctors)
    return render(request,"user/doctors_list.html",{"doctors": doctors})