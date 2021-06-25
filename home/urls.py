from django.contrib import admin
from django.urls import path
from home import views 

urlpatterns = [
   path('', views.home, name ='home'),
   path('listen', views.listen, name ='listen'),
   path('upload', views.upload, name ='upload'),
   path('about', views.about, name ='about'),
   
]
