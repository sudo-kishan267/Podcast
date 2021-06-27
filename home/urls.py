from django.contrib import admin
from django.urls import path
from home import views 

from django.conf import settings
from django.conf.urls.static import static
from django.core.files.storage import FileSystemStorage


urlpatterns = [
   path('', views.home, name ='home'),
   path('listen', views.listen, name ='listen'),
   path('upload', views.upload, name ='upload'),
   path('about', views.about, name ='about'),
   
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
