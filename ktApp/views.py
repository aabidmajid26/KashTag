from django.shortcuts import render,HttpResponse

# Create your views here.


def home(request):
    return render(request, "ktApp/home.html")

def display_huts(request):
    return render(request, "ktApp/huts.html")
def display_hotels(request):
    return render(request, "ktApp/hotels.html")