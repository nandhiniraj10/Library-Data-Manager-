from django.contrib import admin
from django.urls import path
from myapp import views


urlpatterns =[
    path('admin/',admin.site.urls),
    path('hi',views.home),
    path('full',views.full)
]
