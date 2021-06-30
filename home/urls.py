from django.contrib import admin
from django.urls import path
from home import views 

#added latter
from django.conf import settings
from django.conf.urls.static import static
from django.core.files.storage import FileSystemStorage

urlpatterns = [
   path('', views.home, name ='home'),
   path('listen', views.listen, name ='listen'),
   path('watch', views.watch, name ='watch'),
   path('uploadmp3', views.uploadmp3, name ='uploadmp3'),
   path('about', views.about, name ='about'),
   path('uploadmp4', views.uploadmp4, name ='uploadmp4'),
   
]
# changed
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

