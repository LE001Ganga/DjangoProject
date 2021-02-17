from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def static(request):
    return HttpResponse("<center><i style='font-size:50px;background-color:cyan;margin:20px;border-radius:20px;padding-bottom:20px'>This first Static web page from <b style='color:red'>DJANGO</b></i><center>")

def dynamicstr(request,name):
    return HttpResponse("<h3>Hii "+name+"<br>This is dynamic string URL</h3>")
def dynamicint(request,num):
    return HttpResponse("<h1>Pinno is {} <br>for student</h1>".format(num))

def dynamicstrint(request,name,num):
    return HttpResponse("<center><h1>My Name is {} and pinno is 19555A0{}</h1></center>".format(name,num))