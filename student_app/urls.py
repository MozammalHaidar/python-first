from django.urls import path
from .views import *

urlpatterns = [
    path('',myFnc,name='exam'),
    path('first',secFnc,name='first'),   
]