from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Product

# INDEX
def index(request):
    return HttpResponse("Welcome to Django App!")

# HOME
def home(request):
    return HttpResponse("This is the Home Page")

# REGISTER
def register_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if User.objects.filter(username=username).exists():
            return render(request, "register.html",
                          {"error": "Username already exists"})

        user = User.objects.create_user(username=username, password=password)
        login(request, user)
        return redirect("product_list")

    return render(request, "register.html")

# LOGIN
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("product_list")

        return render(request, "login.html",
                      {"error": "Invalid username or password"})

    return render(request, "login.html")

# LOGOUT
def logout_view(request):
    logout(request)
    return redirect("login")

# PRODUCT LIST
@login_required
def product_list(request):
    products = Product.objects.all()
    return render(request, "product.html", {"products": products})

# PRODUCT DETAIL
@login_required
def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, "product_detail.html",
                  {"product": product})

# PRODUCT DATA (you forgot this earlier)
def productdata(request):
    return HttpResponse("Product data endpoint working")