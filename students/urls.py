from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name="index"),
    path('registers/', registers, name='register'),
    path('login/', loginpage, name='login'),
    path('loginact/', loginact, name='loginact'),
    path('test/', test, name='testing'),
    path('Studash/', Studash, name='Studashboard'),
    path('Teacherdash/', Teacherdash, name='Teacherdashboard'),
    path('logout/', logoutend, name='logoutall')
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)