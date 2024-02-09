from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages
from home.models import Contact


def home(request):
    return render(request, 'home.html', {"name": "Sumit"})


def about(request):
    return render(request, 'about.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contact_obj = Contact(name=name, email=email, message=message)
        contact_obj.save()
        messages.success(request, "Message added successfully.")
    return render(request, 'contact.html')


def services(request):
    return render(request, 'services.html')