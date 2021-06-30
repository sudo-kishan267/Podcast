from django.contrib import admin

#Added by me
from home.models import audio, video
# Register your models here.
admin.site.register(audio)
admin.site.register(video)