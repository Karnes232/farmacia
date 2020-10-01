import json
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

from .models import User, Posts, Sales, Inventroy
from .forms import SuperUser

# Create your views here.

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("cogs"))
        else:
            return render(request, "pharmacy/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "pharmacy/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

@login_required(login_url='login')
def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "pharmacy/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "pharmacy/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        current_user = request.user.get_username()
        is_super = SuperUser(current_user)
        return render(request, "pharmacy/register.html", {
            "is_super": is_super
        })

def index(request):
    return render(request, "pharmacy/index.html")

def services(request):
    return render(request, "pharmacy/services.html")

@csrf_exempt
def blog(request):
    #Enables logged in user to delete posts
    if request.method == "POST":
        data = json.loads(request.body)
        post_id = data.get('post_id')
        Posts.objects.filter(id=post_id).delete()
        return HttpResponseRedirect(reverse("blog"))

    #Shows all blog posts 3 per page
    else:
        posts = Posts.objects.all().order_by("-timestamp")
        paginator = Paginator(posts, 3)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, "pharmacy/blog.html", {
            "posts": page_obj
        })

def about(request):
    return render(request, "pharmacy/about.html")

@login_required(login_url='login')
def create(request):
    #Allows logged in user to create blog post
    if request.method == "POST":
        current_user = request.user.get_username()
        current_id = User.objects.get(username=current_user)
        title = request.POST["title"]
        description = request.POST["description"]
        photo_url = request.POST["photourl"]
        p = Posts(user=current_id, title=title, post_body=description, link=photo_url)
        p.save()
        return HttpResponseRedirect(reverse("blog"))
    else:
        current_user = request.user.get_username()
        is_super = SuperUser(current_user)
        return render(request, "pharmacy/create.html", {
            "is_super": is_super
        })

@login_required(login_url='login')
def cogs(request):
    if request.method == "POST":
        sales = request.POST["sales"]
        cost = request.POST["cost"]
        s = Sales(daily_sales=sales, cost=cost)
        s.save()
        return render(request, "pharmacy/index.html")

    else:
        current_user = request.user.get_username()
        is_super = SuperUser(current_user)   
        return render(request, "pharmacy/daily.html", {
            "is_super": is_super
        })

def report(request):
    sales = Sales.objects.all().order_by("-timestamp")
    paginator = Paginator(sales, 30)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    current_user = request.user.get_username()
    is_super = SuperUser(current_user) 
    return render(request, "pharmacy/report.html", {
        "posts": page_obj,
        "is_super": is_super
    })