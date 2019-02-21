from django.shortcuts import render
# from django.http import HtttpResponse

def home(request):
    return render(request, "home.html", {})

def about(request):
    return render(request, "about.html", {})

def contact(request):
    return render(request, "contact.html", {})
    
def base(request):
    return render(request, "base.html", {})

def index(request):
    return render(request, "index.html", {})

def left_sidebar(request):
    return render(request, "left-sidebar.html", {})

def right_sidebar(request):
    return render(request, "right-sidebar.html", {})

def no_sidebar(request):
    return render(request, "no-sidebar.html", {}) 
   
