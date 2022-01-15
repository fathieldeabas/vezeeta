from curses.ascii import US
from django.shortcuts import render ,redirect
from django.contrib.auth.models import User
from .models import Profile
from .forms import Login_Form ,Update_Profile,UserCreationForms
from django.contrib.auth import authenticate ,login
from django.contrib.auth.decorators import login_required
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
@login_required()
def profile(request):
    return render(request,"user/profile.html",{})


def update_profile(request):
    user_form =Update_Profile(instance=request.user)
    if request.method == "POST":
        user_form =Update_Profile(request.POST, instance= request.user)
        if user_form.is_valid():
            user_form.save()
            return redirect('accounts:doctors')
    return render(request,"user/update_profile.html",{"user_form":user_form})

def signup(request):
    if request.method == "POST":
        form= UserCreationForms(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")
            user=authenticate(request,username=username,password=password)
            
            login( request,user)
            return redirect('accounts:doctors')
    else:
        print("rrrr")
        form= UserCreationForms()
    return render(request,"user/signup.html",{"form": form})