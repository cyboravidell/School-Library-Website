from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages



def home(request):
    return render(request, "home.html")

def staffSignin(request):
    if request.method == "POST":

        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']

        user = authenticate(username = loginusername, password = loginpassword)
        if user is None:
            messages.error(request, "Invalid Credentials, Please check and retry again")
            return redirect('home')
        else:
            login(request,user)
            messages.success(request, "Successfully Logged In")
            return redirect('staff')
    else:
        HttpResponse("404 - Not Found")


def staffLogout(request):
    logout(request)
    messages.success(request, "Successfully Logout")
    return redirect('home')