from django.shortcuts import render,redirect


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
    return render(request,'shop-detail.htm')

def wishlist(request):
    return render(request,'wishlist.html')

def Location(request):
    return render(request,'our-location.html')