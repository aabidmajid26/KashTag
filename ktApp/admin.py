from django.contrib import admin

# Register your models here.
from .models import Hut, Hotel, PonyWalla, Instructor, SkiLender,SkiShop, PhoneHotel, PhoneHut, PhoneInstructor, PhonePonyWalla, PhoneSkiLender, PhoneSkiShop

admin.site.register(Hut)
admin.site.register(Hotel)
admin.site.register(PonyWalla)
admin.site.register(Instructor)
admin.site.register(SkiLender)
admin.site.register(SkiShop)
admin.site.register(PhoneHotel)
admin.site.register(PhoneHut)
admin.site.register(PhoneInstructor)
admin.site.register(PhonePonyWalla)
admin.site.register(PhoneSkiLender)
admin.site.register(PhoneSkiShop)