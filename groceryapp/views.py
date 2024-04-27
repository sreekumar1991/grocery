from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from .models import userData 
from django.http import JsonResponse
from pathlib import Path
import os
BASE_DIR = Path(__file__).resolve().parent.parent
from django.contrib.auth import authenticate, login, logout

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

# React page loading index.html.

class ReactPageView(TemplateView):
    template_name = os.path.join(BASE_DIR,'newreact/build/index.html')


def Signup(request):

    if request.method == 'POST':
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        email = request.POST["email"]
        Password1 = request.POST["password1"]
        Password2 = request.POST["password2"]
        Mobile = request.POST["Phone_number"]
        Adhaar = request.POST["Adhaar_Card"]
        genderinfo = request.POST["Gender"]

        if Password1 == Password2:
            if User.objects.filter(username = email).exists():
                  print("username alredy exisit")
                  return render(request,'register2.html')
   
            else:
                # Create the user
                User.objects.create_user(username=email, email=email, password=Password1, first_name=firstname, last_name=lastname)

                # Create the userData object
                userData.objects.create(FirstName=firstname, LastName=lastname, Email=email, Mobile=Mobile, AdhaarCard=Adhaar, Gender=genderinfo)

                # Redirect to the homepage
                return redirect('/')

        else:
             print("password not match")
             return redirect('/register/')   
    else:
         return render(request,'register2.html')
    
    

def user_data(request):
    # fetching all the objects from UserData class
    users = userData.objects.all()
    serialized_data = [{'FirstName': user.FirstName, 'LastName': user.LastName, 'Email': user.Email, 'Phone': user.Mobile, 'AdhaarCard': user.AdhaarCard} for user in users]
   
    # If you want to return JSON response
    return JsonResponse({'user_data': serialized_data})
    


def Login_view(request):
    if request.method == 'POST':
        # Assuming your form has 'username' and 'password' fields
        username = request.POST.get('Username')
        password = request.POST.get('Password')

        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            # Redirect to a success page, or somewhere else
            print("log in success")
            return redirect('/account/')  # Assuming 'home' is another URL pattern
        else:
            # Return an error message if authentication fails
            # messages.error(request, 'Invalid username or password.')
            # You can redirect back to the login page or render it again with the form
            print("log in failed")
            return redirect('/sign-in/')  # Assuming 'login' is the name of the login page
    else:
        # If the request method is GET, render the login form
        return render(request, 'Sign-in1.html')  # Assuming you have a template named 'login.html' for the login page
    




