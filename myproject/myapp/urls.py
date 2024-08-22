from django.urls import path
from . import views

urlpatterns =[
     path('hii/',views.home),
     path('products/',views.product)
    
     
]
