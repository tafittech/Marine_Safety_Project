from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render

from django.conf import settings
from django.conf.urls.static import static




# --cover page view ---

def coverPage(request):
    return render(request, 'index.html',{})



#---urls patterns-------

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', coverPage, name='home' ),
    path('', include('Admin.urls')),
    path('', include( 'Students.urls')),
    path('', include('messageCenter.urls')),
]






#---static urls patterns-----

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
