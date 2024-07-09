from django.shortcuts import render

from django.http import HttpResponse       

def home(request):
    # return HttpResponse("Hey I am a django users")
    return render(request,"index.html")

def success_page(request):
    return HttpResponse("<h1>Success</h1>")