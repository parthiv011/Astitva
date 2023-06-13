from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import authenticate,login
from .models import User
from django.contrib import messages

# Create your views here.
def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        
        if confirm_password != password:
            return HttpResponse('Passwords do not match')
        else:
            user = User.objects.create_user(email=email, password=password, first_name=first_name, last_name=last_name, username=username)
            messages.success(request, 'Account created successfully.')
            return redirect('login')

    return render(request, 'register.html')
    
# Login and Signup will be updated with JWT Authentication using RestFramework in Django

def logIn(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user = authenticate(request, email=email, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid email or password.')
            return redirect('login')
    return render(request, 'login.html')


def home(request):
    return render(request,'home.html')

def platform(request):
    return render(request,'platforms.html')


