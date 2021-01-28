from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login ,logout
from django.contrib import messages

# Create your views here.
def loginUser(request):
    username= request.POST.get('username', '')
    password= request.POST.get('password', '')
    user = authenticate(username=username, password=password)
    if user is not None:
        # A backend authenticated the credentials
        login(request, user)
        messages.success(request, "Login Successful")
        return redirect(content)
        
        
    else:
        # No backend authenticated the credentials
        messages.error(request, "Wrong username or password")
        return redirect('Login-SignUp')
        
def register(request):
    fullName= request.POST.get('fullName', '')
    temp=fullName.split(' ')
    
    firstName=temp[0]
    lastName=temp[1]
    
    username= request.POST.get('username', '')
    email= request.POST.get('email', '')
    password= request.POST.get('password', '')

    user=User.objects.create_user(username, email, password)
    user.first_name= firstName
    user.last_name=lastName
    user.save()
    login(request, user)
    messages.success(request, "Account Created Successfully")
    

    return redirect(content)




def index(request):
    context={}
    return render(request, 'userAuthapp/index.html', context)

def content(request):
    
    return render(request, 'userAuthapp/content.html',{})


def logoutUser(request):
    logout(request)
    messages.success(request, "Logout Successful")
    return redirect('Login-SignUp')
