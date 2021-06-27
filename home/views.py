from django.db.models.fields import files
from home.models import uploads
from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponse 
 
#added by me
from datetime import datetime
from django.contrib import messages
from django.core.files.storage import FileSystemStorage

# import your model here

from django.contrib import messages

# Create your views here.
def home(request):
    return render(request,'home.html')
    
    
def listen(request):
    return render(request,'listen.html')

def upload(request):
    if request.method =="POST" :
         name = request.POST.get('name')
         pname = request.POST.get('pname')
         email = request.POST.get('email')
         mp3 = request.FILES['mp3']
         fs=FileSystemStorage()
         info = uploads(name=name, pname=pname, email=email, mp3=mp3, date=datetime.today())
         info.save()
         
         messages.success(request, 'Podcast Uploaded !')

    return render(request,'upload.html')


def about(request):
    return render(request,'about.html')