from django.db.models.fields import files
from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponse 
 
#added by me
from datetime import datetime         # for storing current date and time while uploading files
from django.contrib import messages   # for succes message after uploading 
from django.core.files.storage import FileSystemStorage    # for uploading file to a particular(media) directory

# import your model here
from home.models import audio        # imported our 'audio' database form models.py
from home.models import video        # imported our 'video' database form models.py 


# Create your views here.
def home(request):
    return render(request,'home.html')
    
    
def listen(request):
    mp3_list= audio.objects.all()        # calling 'audio' database from models.py and storing it in dic mp3_list 
    return render(request,'listen.html',{'mp3_list':mp3_list})    # rendering the page and sending the dic to page
                                                                       

def watch(request):
    mp4_list= video.objects.all()          # calling 'video' database from models.py and storing it in dic mp4_list
    return render(request,'watch.html',{'mp4_list':mp4_list})      # rendering the page and sending the dic to page

def uploadmp3(request):
    if request.method =="POST" :        # if uploadmp3 page is requested through POST method
         name = request.POST.get('name')
         pname = request.POST.get('pname')
         email = request.POST.get('email')
         mp3 = request.FILES['mp3']
         FileSystemStorage()                    # saved the file in media directory by default
         info = audio(name=name, pname=pname, email=email, mp3=mp3, date=datetime.today())
         info.save()
         
         messages.success(request, 'Podcast Uploaded !')

    return render(request,'uploadmp3.html')


def uploadmp4(request):
    if request.method =="POST" :           # if uploadmp4 page is requested through POST method
         name = request.POST.get('name')
         pname = request.POST.get('pname')
         email = request.POST.get('email')
         mp4 = request.FILES['mp3']
         FileSystemStorage()                # saved the file in media directory by default
         info = video(name=name, pname=pname, email=email, mp4=mp4, date=datetime.today())
         info.save()
         
         messages.success(request, 'Podcast Uploaded !')

    return render(request,'uploadmp4.html')

def about(request):
    return render(request,'about.html')