from django.shortcuts import render,HttpResponse
from django.http import JsonResponse

# Create your views here.
from .models import Hut, Hotel, SkiLender, SkiShop, PonyWalla, Instructor
model = {
    'hut' : Hut,
    'hotel' : Hotel,
    'ski-shop': SkiShop,
    'sledge' : PonyWalla,
    'ski-lender' : SkiLender,
    'instructor' : Instructor,
    'ski' : SkiShop
}

def home(request):
    return render(request, "ktApp/home.html")

def display(request, activity):
    allObjects = model[activity].objects.all()
    objs = [obj.serialize() for obj in allObjects]
    l = len(objs)-(len(objs)%3)
    objs = objs[:l]
    return JsonResponse(objs, safe=False)
    

