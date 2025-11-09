from django.shortcuts import render
from myapp.models import Contact
from django.http import HttpResponse


def index(request):
    return render(request , 'index.html')

def contact_us(request):
    if request.method=="POST":
        name=request.POST.get("name")
        em = request.POST.get("email")
        sub=request.POST.get("subject")
        msz=request.POST.get("message")

        obj=Contact(name=name, email=em, subject=sub,message=msz)
        obj.save()
        return HttpResponse("Dear {name}, Thanks for your time!")
    return render(request, 'contact.html')

def about(request):
    return render(request,'about.html')

def team(request):
    return render(request, 'team.html')

from django.shortcuts import render

def register(request):
    return render(request, 'register.html')  

# def team(request):
#     return render(request, 'all_dishes.html')