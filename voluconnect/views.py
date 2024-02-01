from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html", {})

def blog_details(request):
    return render(request, "blog_details.html", {})

def blog(request):
    return render(request, "blog.html", {})

def contact(request):
    return render(request, "contact.html", {})

def courses(request):
    return render(request, "courses.html", {})

def elements(request):
    return render(request, "elements.html", {})

def login(request):
    return render(request, "login.html", {})

def register(request):
    return render(request, "register.html", {})