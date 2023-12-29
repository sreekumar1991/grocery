from django.shortcuts import render,redirect
from .models import userData
from django.http import HttpResponse
import json
from django.core.serializers import serialize
from django.http import JsonResponse

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
        userdata = request.POST.get("firstname")

        # data = userData.objects.all() # to fetch all the data from database
        # return render(request,'register.html',{"data":data})
        # data = serialize('json', userData.objects.all())  # Convert data to JSON
        return HttpResponse(userdata, content_type='application/json')



# def Signup(request):
#     if request.method == 'POST':
#         firstname =  request.POST.get("firstname")
#         lastname = request.POST.get("lastname")
#         email = request.POST.get("email")
#         pancard = request.POST.get("pan")
#         debitcard = request.POST.get("credit/debit")
#         password = request.POST.get("password1")
#         confirm_password = request.POST.get("password2")

#         alldtata = {"name":firstname,"inital":lastname,"mailID":email,"pandetails":pancard,"cc": debitcard,"pass":password,"pass2":confirm_password}
#         data = json.dumps(alldtata)
#         # data = userData.objects.all() # to fetch all the data from database
#         # return render(request,'register.html',{"data":data})
#         # data = serialize('json', userData.objects.all())  # Convert data to JSON

#         return  JsonResponse(data, content_type='application/json'),
         
        