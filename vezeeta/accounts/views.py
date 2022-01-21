from curses.ascii import US
from email import message
import email
import json
from math import ceil, floor
from django.shortcuts import render ,redirect
from django.contrib.auth.models import User
from .models import Profile , Order,Comments,rate
from .forms import Login_Form ,Update_Profile,UserCreationForms,Update_Profile2,order_form,CommentForm,RateForm
from django.contrib.auth import authenticate ,login,logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .filter import DoctorFilter
from django.core.mail import send_mail
from django.conf import settings
from django.db.models import Avg
# Create your views here.
def docter_list(request):
    _doctors= Profile.objects.all()
    
    filter = DoctorFilter(request.GET, queryset=_doctors)
    doctors = filter.qs
    # doctors= Profile.objects.all()
    for doctor in doctors:
        
        print(doctor.rate.all())
        a=doctor.rate.all()
        average=0
        sum=0
        for rate in a:
            print(rate.rate_doctor)
            sum=sum+int(rate.rate_doctor)
            print("#################")
        if len(a)==0:
            average=0
        else:
            average=sum/len(a)
        print(ceil(average))
        doctor.ff=ceil(average)
    print(doctors)
    return render(request,"user/doctors_list.html",{"doctors": doctors, "filter":filter})

def docter_details(request,slug):
    new_comment = None
    doctors_details= Profile.objects.get(slug=slug)

    if request.method == 'POST':
        _email= request.POST["email"]
        order_name=Order.objects.filter(patient_email=_email,profile=doctors_details).first()
        in_rate= rate.objects.filter(email=_email,doctor=doctors_details).first()
        
        if in_rate is  None :
            if order_name is not  None :

                print(in_rate)
        # ######################## To Add rate ##############################    

                rateForm=RateForm(data= request.POST) 
                if rateForm.is_valid():
                    new_rate=rateForm.save(commit=False)
                    new_rate.order = order_name
                    new_rate.doctor=doctors_details
                    new_rate.save()
                    rateForm=RateForm()
                    message="شكرا علي تقيمك"

            else:
                rateForm=RateForm()
                message="لم يمكن التقييم بدون حجز عند الدكتور"


        else:
            rateForm=RateForm()
            message="لقد تم التقيم مسبقا"

        # ######################## To Add Comments ##############################    

        commentform = CommentForm(data=request.POST)
        if commentform.is_valid():
            # Create Comment object but don't save to database yet          
            new_comment = commentform.save(commit=False)
            # Assign the current post to the comment
            new_comment.doctor = doctors_details
            # Save the comment to the database
            new_comment.save()
            commentform = CommentForm()
        else:
            pass
        ###############################################
    
        
    else:
        message=None
        commentform = CommentForm()
        rateForm=RateForm()
        
    comments =Comments.objects.filter(doctor=doctors_details.id)
   

    return render(request,"user/doctors_details.html",{"doctors_details": doctors_details,'commentform': commentform,'comments': comments,"rateForm":rateForm,"message":message,})

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
    user_form2 =Update_Profile2(instance=request.user)

    if request.method == "POST":
        user_form =Update_Profile(request.POST, instance= request.user)
        user_form2 =Update_Profile2(request.POST,request.FILES, instance= request.user)

        if user_form.is_valid() and user_form2.is_valid():
            user_form.save()
            user_form2.save()
            return redirect('accounts:doctors')
    return render(request,"user/update_profile.html",{"user_form":user_form,'user_form2':user_form2})

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


def logout_view(request): 
    logout(request)
    return redirect('accounts:login')


def make_order(request,slug):
    form=order_form()
    doctors_details= Profile.objects.get(slug=slug)
    return render(request,"user/make_order.html",{"doctors_details": doctors_details,"form":form})



def order_complete(request):
   
    body = json.loads(request.body)
    message= "\n {0}{1}".format(" استاذ "+body['patient'] + ""," لقد تم حجز معاد الساعه:"+body['date']) 
    profile=Profile.objects.get(user=body['doctor'])
    Order.objects.create(patient=body['patient'],profile=profile,date=body['date'],patient_email=body['email'],completed=True)
    send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [body['email']],
        )
    return redirect('accounts:doctors')

