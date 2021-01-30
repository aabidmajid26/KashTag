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
def displayIndividual(request, activity, fid):
    
    allObjects = model['activity'].objects.filter(id=fid)
    if activity == 'ski' or 'ski-shop' or 'hut' or 'hotel':
        return JsonResponse([obj.serialize() for obj in allObjects], safe = False)
    else:
        return JsonResponse({'Id': 'Jello Jorld'}, safe=False)
    

