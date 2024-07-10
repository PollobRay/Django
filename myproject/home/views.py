from django.shortcuts import redirect, render

from django.http import HttpResponse   
from home.models import Student    

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

def view_data(request):
    students= Student.objects.all()
    return render(request,"view_database.html",context={'students':students})  # passes all student object

def add_student(request):
    if request.method == "POST":
        std =   Student(
            name    =   request.POST.get("name"),
            email   =   request.POST.get("email"),
            age     =   request.POST.get("age")
        )
        std.save()          # store to Database

        return redirect('view_data')
    return render(request,"add_student.html")

def update_student(request,id):             # here 'id' and url 'id' must be same
    return render(request,"update_student.html")