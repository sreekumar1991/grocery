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
        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")
        email = request.POST.get("email")
        pancard = request.POST.get("pan")
        debitcard = request.POST.get("credit/debit")
        passwrd = request.POST.get("password1")
        confirm_passwrd = request.POST.get("password2")

        user = User.objects.create_user(username=email, email=email, password=passwrd)
        user.first_name = firstname
        user.last_name = lastname
        user.save()

        user_data = userData(FirstName=firstname, LastName=lastname, Email=email, PanCard=pancard, AdhaarCard=debitcard)
        user_data.save()

    #     data = userData.objects.all()
    #     serialized_data = [{'FirstName': user.FirstName, 'LastName': user.LastName, 'Email': user.Email, 'PanCard': user.PanCard, 'AdhaarCard': user.AdhaarCard} for user in data]
    #     return JsonResponse({'user_data': serialized_data})
    #     # Return data as JSON response


    # elif request.method == 'GET':
    #     # Handle GET requests (e.g., render the signup form)
    #    return render(request, 'X.html', {"data": data}) # Adjust the template name as needed

    # else:
    #     # Handle other HTTP methods if needed
    #     return HttpResponse("Method Not Allowed", status=405)


# def getuserdata(request):
#             data = userData.objects.all()
#             serialized_data = [{'FirstName': user.FirstName, 'LastName': user.LastName, 'Email': user.Email, 'PanCard': user.PanCard, 'AdhaarCard': user.AdhaarCard} for user in data]
#             # return JsonResponse({'user_data': serialized_data})
#             return TemplateView.as_view(template_name=os.path.join(BASE_DIR, 'newreact/build/index.html'))(request, user_data=serialized_data)


        # Return data as JSON response
# this is the code to  retrieve all the data from database 
    # data = userData.objects.all()
    # serialized_data = [{'FirstName': user.FirstName, 'LastName': user.LastName, 'Email': user.Email, 'PanCard': user.PanCard, 'AdhaarCard': user.AdhaarCard} for user in data]
    # return JsonResponse({'user_data': serialized_data})
    