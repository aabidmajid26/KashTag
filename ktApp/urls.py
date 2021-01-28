from django.urls import path
from . import views

app_name = 'ktApp'


urlpatterns = [
    path('', views.home, name='home'),
    path('display-huts/', views.display_huts, name='display-huts'),
    path('display-hotels/', views.display_hotels, name='display-hotels'),
]