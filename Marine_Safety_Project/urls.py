from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render

from django.conf import settings
from django.conf.urls.static import static




# --cover page view ---




#---urls patterns-------

urlpatterns = [
    path('admin/', admin.site.urls, name='apanel'),
    path('', include('Admin.urls')),
    
]






#---static urls patterns-----

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
