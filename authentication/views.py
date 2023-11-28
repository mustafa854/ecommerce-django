from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import  User
from django.contrib.auth.decorators import login_required

def signin(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('/')
        else:
            print('hi')
            messages.error(request, 'Bad Credentials!')
    return render(request, 'authentication/signin.html')


def signup(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        context={
            'first_name':first_name,
            'last_name':last_name,
            'username':username,
            'email':email,
        }
        if password1==password2:
            username_exists = User.objects.filter(username=username)
            if username_exists:
                messages.error(request,"Username Exists! Please choose a different username.")
                return render(request, 'authentication/register.html', {'context':context})
            else:
                email_exists = User.objects.filter(email=email)
                if email_exists:
                    messages.error(request,"Username Exists! Please choose a different username.")
                    return render(request, 'authentication/register.html', {'context':context})
                else:
                    user = User.objects.create_user(username=username, email=email, password=password1, first_name=first_name, last_name=last_name)
                    login(request, user)
                    return redirect('/')
        else:
            messages.error(request,"Passwords doesn't match")
            return render(request, 'authentication/register.html', {'context':context})
    return render(request, 'authentication/register.html')

@login_required(login_url='/auth/login')
def signout(request):
    logout(request)
    return redirect('/')