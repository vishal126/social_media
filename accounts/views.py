from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import *
from django.core.mail import send_mail
import random
from django.contrib import messages
from django.conf import settings
from feed.models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login,logout
from feed.views import *



# Create your views here.
#buisness logic

@login_required
def hello(request):
    return render(request,"index.html")

def home(request):
    return render(request,'hello.html')







def Login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
        
            return redirect('feed:home')
        else:
            messages.error(request,'Invalid cridential')
            return redirect("Login")
    
    return render(request,"login.html")

"""def email(request):
    form = Email_sender(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            from_email = "gauravnagda583@gmail.com"
            to_email = form.cleaned_data['to_email']
            print(subject)
            print(message)
            send_mail(subject,message,from_email,[to_email])
            return HttpResponse(request,"Email sent successfully")
        else:
            form= Email_sender()
    return render(request, "email.html", {"form": form})"""



"""def basic_form(request):
    if request.method =="POST":
        # 
        form = SimpleForm(request.POST, request.FILES)
        # from forms .py we are importing simple form
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data["message"]
            image = form.cleaned_data['image']
            print(name)
            print(message)
            print(email)
            print(image)
            return HttpResponse("Thank Your")
        
    else:
        form = SimpleForm()
    return render(request, "name.html", {"form": form})
"""

       
def Logout(request):
    logout(request)
    return redirect("accounts:login")



def register(request):
    if request.method=="POST":
        username = request.POST["username"]
        password = request.POST["password"]
        print(username)
        print(password)

        if User.objects.filter(username=username).exists():
            messages.error(request,"Username Already exist")
            return redirect("accounts:register")

        user = User.objects.create_user(username=username, password=password)
        user.save()
        #login(request,user)
        return redirect("feed:home")
        
    
    return render(request,"login_dynamic.html")




"""
def Login_otp(request):
    if request.method == "POST":
        data = request.POST
        email = data.get('email')
        print(email)

        otp = random.randint(100000,999999)
        

        # to verify otp 
        request.session['otp'] = otp
        request.session['email'] = email



        # send otp using mail 
        subject = "OTP From django website"
        message = f"Your otp is here :-> {otp}"
        from_email = settings.EMAIL_HOST_USER

        send_mail(subject,message,from_email,[email])
        return redirect('verify_otp')
    
    return render(request,"login_otp.html")"""



def verify_otp(request):
    if request.method == "POST":
        data = request.POST
        user_otp = data.get('user_otp')

        send_otp = request.session.get('otp')


        if str(user_otp)==str(send_otp):
            messages.success(request,"otp is Verified sucessfully")
            return redirect('home')
        else:
            messages.error(request, "Invalid Otp")
            
    return render(request,"verify_otp.html")



# Jinja 
"""
    Jinja is a templating engine in python 
    with the help of jinja we can write the python code to html xml


    name = "gaurav"

    how ?
    {{name}}

    # conditional 
        {% if condition %}
        # code to be executed if condition is true
        {% endif %}


        {%if condtion % }
        # code to be executed if condition is true
        {% else %}
        # code to be executed if condition is false
        {% endif %}

        {%if condition %}
        # code to be executed if condition is true
        {% elif condition %}
        # code to be executed elif condition is true
        {%else %}
        # code to be executed if all conditions are false
        {% endif %}


"""


"""
LOOPS in Jinja 
# for loop
{% for item in list %}
# code to be executed for each item in list
{%endfor %}


"""


"""
{% load static %}
"""
