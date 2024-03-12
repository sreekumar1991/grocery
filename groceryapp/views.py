from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import userData 
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.generic import TemplateView
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
import os

def index(request):
    return render(request,'index.html')

# Create your views here.

def shop(request):
    return render(request,'shop.html')

def about(request):
    return render(request,'about.html')

def cart(request):
    return render(request,'cart.html')

def checkout(request):
    return render(request,'checkout.html')

def contactus(request):
    return render(request,'contact-us.html')

def gallery(request):
    return render(request,'gallery.html')

def shopdetails(request):
    return render(request,'shop-detail.html')

def wishlist(request):
    return render(request,'wishlist.html')

def Location(request):
    return render(request,'our-location.html')

def Signin(request):
    return render(request,'Sign-in1.html')

def Register(request):
    return render(request,'register.html')



def Signup(request):
    if request.method == 'POST':
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        email = request.POST["email"]
        Mobile = request.POST["Phone_number"]
        Adhaar = request.POST["Adhaar_Card"]

        user = User.objects.create_user(username=email, email=email)
        user.first_name = firstname
        user.last_name = lastname
        user.save()

        user_data = userData(FirstName=firstname, LastName=lastname, Email=email,  Mobile=Mobile, AdhaarCard=Adhaar)
        user_data.save()

        return redirect('/')     
    else:
        return render(request,'register.html') 
    

def getuserdata(request):
    users = userData.objects.all()
    serialized_data = [{'FirstName': user.FirstName, 'LastName': user.LastName, 'Email': user.Email, 'Phone': user.Mobile, 'AdhaarCard': user.AdhaarCard} for user in users]
    
    # If you want to return JSON response
    # return JsonResponse({'user_data': serialized_data})
    
    # If you want to render a template with the serialized data
    template_path = os.path.join(BASE_DIR, 'newreact/build/index.html')
    return TemplateView.as_view(template_name=template_path)(request, user_data=serialized_data)