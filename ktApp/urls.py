from django.urls import path
from . import views

app_name = 'ktApp'


urlpatterns = [
    path('', views.home, name='home'),
    path('display/<str:activity>/', views.display, name='display'),
]