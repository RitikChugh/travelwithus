from django.shortcuts import render 
from django.http import HttpResponse
from .models import destination

def index(request):


    dests=destination.objects.all()

    return render (request,"index.html",{'dests':dests})
     
def about(request):

    return render (request,"about.html")

def contact(request):
    return render (request,"contact.html")


def destinations(request):
    dests=destination.objects.all()
    return render (request, "destinations.html",{'dests':dests})

# Create your views here.