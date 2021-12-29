from django.shortcuts import render,HttpResponse
from django.http import JsonResponse

# Create your views here.
from .models import Hut, Hotel, SkiLender, SkiShop, PonyWalla, Instructor
from .models import PhoneHotel, PhoneHut, PhoneInstructor, PhonePonyWalla, PhoneSkiLender, PhoneSkiShop
model = {
    'hut' : Hut,
    'hotel' : Hotel,
    'ski-shop': SkiShop,
    'sledge' : PonyWalla,
    'ski-lender' : SkiLender,
    'instructor' : Instructor,
    'ski' : SkiShop
}
modelPhone = {
    'hut' : PhoneHut,
    'hotel' : PhoneHotel,
    'ski-shop': PhoneSkiShop,
    'sledge' : PhonePonyWalla,
    'ski-lender' : PhoneSkiLender,
    'instructor' : PhoneInstructor,
    'ski' : PhoneSkiShop
}
def home(request):
    return render(request, "ktApp/home.html")

def display(request, activity):
    allObjects = model[activity].objects.all()
    objs = [obj.serialize() for obj in allObjects]
    L = len(objs)
    if L>3:
        L = L-(L%3)
    objs = objs[:L]
    return JsonResponse(objs, safe=False)
def displayIndividual(request, activity, fid):
    
    allObjects = model['activity'].objects.filter(id=fid)
    if activity == 'ski' or 'ski-shop' or 'hut' or 'hotel':
        return JsonResponse([obj.serialize() for obj in allObjects], safe = False)
    else:
        return HttpResponse("nothing here.")

def getPhone(request, activity, fid1):
    obj = modelPhone[activity].objects.get(fid=fid1)
    x = obj.serialize()
    phoneNumber = x['phoneNumber']
    return HttpResponse(phoneNumber)

