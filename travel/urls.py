
from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index,name="index"),
    path('about/', views.about,name="about"),
    path('contact/', views.contact,name='contact'),
    path('destinations/',views.destinations,name='destinations'),
    

]
urlpatterns=urlpatterns + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)