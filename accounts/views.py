from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['pass']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid Username or Password !')
            return redirect('login')
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('login')


def register(request):
    if request.method == 'POST':
        name = request.POST['name']
        username = request.POST['username']
        password1 = request.POST['password']
        password2 = request.POST['re_password']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username exists !')
                return redirect('register')
            else:
                user = User.objects.create_user(first_name=name, username=username, password=password1)
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'Password not Matching !')
        return redirect('register')

    else:
        return render(request, 'register.html')
