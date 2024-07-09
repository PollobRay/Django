from django.shortcuts import render

from django.http import HttpResponse       

def home(request):
    # return HttpResponse("Hey I am a django users")
    # return render(request,"index.html")

    users=[
        {'name':'Pollob', 'age':24},
        {'name':'Ray', 'age':24},
        {'name':'Dipto', 'age':26},
        {'name':'Kanak', 'age':25}
    ]

    return render(request,"index.html", context={'peoples':users, 'page':'Home Page'})

def about (request):
    return render(request,"about.html",context={'page':'About Page'})

def services (request):
    return render(request,"services.html",context={'page':'Services Page'})