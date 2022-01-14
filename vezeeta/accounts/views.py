from curses.ascii import US
from django.shortcuts import render ,redirect
from django.contrib.auth.models import User
from .models import Profile
from .forms import Login_Form
from django.contrib.auth import authenticate ,login
# Create your views here.
def docter_list(request):
    doctors= User.objects.all()
    # doctors= Profile.objects.all()
    print(doctors)
    return render(request,"user/doctors_list.html",{"doctors": doctors})

def docter_details(request,slug):
    doctors_details= Profile.objects.get(slug=slug)
    return render(request,"user/doctors_details.html",{"doctors_details": doctors_details})

def login_user(request):
    if request.method == "POST":
        form= Login_Form()
        username=request.POST["username"]
        password=request.POST["password"]
        user=authenticate(request,username=username,password=password)
        print("ttttt")
        if user is not None:
            login( request,user)
            return redirect('accounts:doctors')
    else:
        print("rrrr")
        form= Login_Form()
    return render(request,"user/login.html",{"form": form})

def profile(request):
    return render(request,"user/profile.html",{})