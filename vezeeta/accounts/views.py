from curses.ascii import US
from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Profile
from .forms import Login_Form
# Create your views here.
def docter_list(request):
    doctors= User.objects.all()
    # doctors= Profile.objects.all()
    print(doctors)
    return render(request,"user/doctors_list.html",{"doctors": doctors})

def docter_details(request,slug):
    doctors_details= Profile.objects.get(slug=slug)
    return render(request,"user/doctors_details.html",{"doctors_details": doctors_details})

def login(request):
    if request.method=="Post":
        form= Login_Form()
        username=request.POST["username"]
        password=
        return render(request,"user/login.html",{"form": form})