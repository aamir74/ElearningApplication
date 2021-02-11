from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.http import HttpResponse
from .models import video
import os.path

# Create your views here.


def home1(request):
    if request.method == 'POST':
        search = request.POST['search']

        if video.objects.filter(name__icontains=search).exists():

            a = video.objects.get(name__icontains=search)

            return render(request, 'search.html', {'a': a})
        else:
            return render(request, 'notfound.html')

    else:
        return render(request, 'home1.html')


def search(request):
    return render(request, 'search.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return render(request, 'home1.html')
        else:
            messages.info(request, 'invalid credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('login')


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        user_name = request.POST['user_name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=user_name).exists():
                messages.info(request, 'username already exists')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'email already taken')
                return redirect('register')
            else:
                user = User.objects.create_user(
                    username=user_name, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save()
                messages.info(request, 'USER CREATED')
        else:
            messages.info(request, 'password not matched')
            return redirect('register')

        return redirect('/')

    else:
        return render(request, 'register.html')


def class6(request):
    return render(request, 'class6.html')


def maths(request):

    videos = video.objects.all()
    return render(request, 'maths.html', {'videos': videos})


def uvideo(request):
    if request.method == 'POST':
        name = request.POST['name']
        vdo = request.FILES['vdo']
        Class = request.POST['Class']
        subject = request.POST['subject']

        v_obj = video(name=name, videofile=vdo,
                      class_name=Class, subject=subject)
        v_obj.save()
        messages.info(request, 'Solution Added')
        return redirect('maths')
    else:
        return render(request, 'uvideo.html')
