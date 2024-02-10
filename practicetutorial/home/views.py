from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import auth
from home.models import Contact, Customer


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


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.warning(request, "Invalid Credentials")
            return redirect('login')

    return render(request, 'login.html')


def signup(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 == password2:
            if Customer.objects.filter(name=name).exists():
                messages.warning(request, "Username is already taken.")
            elif Customer.objects.filter(email=email).exists():
                messages.warning(request, "email is already taken.")
            else:
                messages.success(request, "User Created")
                customer = Customer(name=name, email=email, password=password1)
                customer.save()
                return redirect('login')
        else:
            messages.warning(request, "Passwords do not match")
    return render(request, "logup.html")

def logout(request):
    auth.logout(request)
    return redirect("/")
