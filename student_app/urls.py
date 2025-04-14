from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name='home'),
    path('exam',myFnc,name='exam'),
    path('first',secFnc,name='first'),    
    path('main',main,name='main'),
    path('delete_proof/<int:prime_id>/', delete_proof, name='delete_proof'),
    path('update_proof/<int:prime_id>/', update_proof, name='update_proof'),
]