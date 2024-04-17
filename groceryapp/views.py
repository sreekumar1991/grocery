from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
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
    return render(request,'register2.html')

def Signup(request):
    if request.method == 'POST':
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        email = request.POST["email"]
        Mobile = request.POST["Phone_number"]
        Adhaar = request.POST["Adhaar_Card"]
        genderinfo = request.POST["Gender"]

        user = User.objects.create_user(username=email, email=email)
        user.first_name = firstname
        user.last_name = lastname
        user.save()

        user_data = userData(FirstName=firstname, LastName=lastname, Email=email,  Mobile=Mobile, AdhaarCard=Adhaar, Gender=genderinfo)
        user_data.save()

        return redirect('/')     
    else:
        return render(request,'register2.html')
    
def user_data(request):
    # fetching all the objects from UserData class
    users = userData.objects.all()
    serialized_data = [{'FirstName': user.FirstName, 'LastName': user.LastName, 'Email': user.Email, 'Phone': user.Mobile, 'AdhaarCard': user.AdhaarCard} for user in users]
   
    # If you want to return JSON response
    return JsonResponse({'user_data': serialized_data})
    






# USER AUTHENTICATON should be in another seperate django app.

# @login_required  # this is used for only allowing for authenticated users and this view only execute for authenticated users 
def account(request):
    template_path = os.path.join(BASE_DIR, 'newreact/build/index.html')
    return render(request, template_path)
    # return TemplateView.as_view(template_name=template_path)(request)
  


# TEST for user authentication ERORR IN THIS CODE 
def login_test(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            # return redirect('success_url')
            return redirect('/')  
            # template_path = os.path.join(BASE_DIR, 'newreact/build/index.html')
            # return TemplateView.as_view(template_name=template_path)(request)
        else:
            # Return an 'invalid login' error message.
            return render(request, 'register2.html', {'error_message': 'Invalid username or password.'})
    else:
        # Display the login form.
        return render(request,'Sign-in1.html')
    













