from django.shortcuts import render, redirect
from django.http import HttpResponse
from home.models import Contact,Info
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


# Create your views here.

def index(request):
    return render(request, "index.html")
    #return HttpResponse("it is index")

def cars(request):
    return render(request, "cars.html")

def login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        pass1 = request.POST.get('password')  
        user = authenticate(username=email, password=pass1)
        if user is not None:
            print(1)
            return redirect("/home")
        else:
            return render(request, "login.html")


    return render(request, "login.html")

def contactUs(request):
    if request.method == "POST":
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        query = request.POST.get('query')
        contact = Contact(email = email,phone = phone, query = query)
        contact.save()



    return render(request, "contact.html")

def signUp(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('pass')
        confPass = request.POST.get('conf_pass')
       
        if password != confPass:
            
            return render(request,"signup.html")
        else:
            user = User.objects.create_user(email,email, password)
            user.save()
            return redirect("/login")

        
    return render(request, "signup.html")

#buckumister@gmail.com
#123456789
