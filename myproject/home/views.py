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


def update_student(request,id):             # id is passed through url, here 'id' and url 'id' must be same
    std=Student.objects.get(pk=id)  # pk means primary key

    if request.method == "POST":
        std.name = request.POST.get("name")
        std.email = request.POST.get("email")
        std.age = request.POST.get("age")
        std.save()
        return redirect('view_data')        # if it is post request then update and redirect
    
    return render(request,"update_student.html", context={'std':std})

def delete_student(request):
    if request.method == "GET":
        id = request.GET.get('id')
        std=Student.objects.get(pk=id)
        std.delete()
        return redirect('view_data')
    return render(request,"delete_student.html")