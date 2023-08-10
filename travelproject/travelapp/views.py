from django.http import HttpResponse
from django.shortcuts import render
from . models import Places
from .models import Themes

# Create your views here.
def demo(request):
    obj=Places.objects.all()
    obj1=Themes.objects.all()
    return render(request,"index.html",{'result':obj,'last':obj1})



