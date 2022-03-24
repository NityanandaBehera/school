import re
from django.shortcuts import redirect, render
from django.http import request
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.


def index(request):
    return render(request, 'students/index.html')


def registers(request):
    if request.method == "POST":

        fname = request.POST['fname']
        lname = request.POST['lname']
        username = request.POST['uname']
        imgs = request.FILES['imgs']
        email = request.POST['email']
        temppass = request.POST['pass']
        password = request.POST['password']
        address = request.POST['address']
        city = request.POST['city']
        state = request.POST['state']
        pincode = request.POST['pincode']
        utype = request.POST['usertypes']

        if password != temppass:
            messages.add_message(request, messages.ERROR,
                                 "Password does not match!!")
        else:
            User.objects.create_user(
                username=username, password=password).save()
            lastobject = len(User.objects.all())-1
            UserDetNew(id=User.objects.all()[int(lastobject)].id, fname=fname, lname=lname, username=User.objects.all()[int(lastobject)].username, email=email, password=User.objects.all()[
                       int(lastobject)].password, address=address, city=city, state=state, pincode=pincode, usertype=utype, profile_pic=imgs).save()

            fresult = "Details Stored Successfully!! Thank You"

            return render(request, 'students/register.html', {'status': fresult})

    return render(request, 'students/register.html')


def loginpage(request):
    return render(request, 'students/login.html')


def loginact(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # types = request.POST['usertypes']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            current_user = request.user
            ids = current_user.id
            r = UserDetNew.objects.get(pk=ids)
            if r.usertype == 'Student':
                return redirect('Studashboard')
            else:
                return redirect('Teacherdashboard')
        else:
            return redirect('login')


def test(request):
    return render(request, 'students/test.html')


def Studash(request):
    context = {'studetails': UserDetNew.objects.filter(
        username=request.user.username)}
    return render(request, 'students/studashboard.html', context)


def Teacherdash(request):
    context = {'teacherdetails': UserDetNew.objects.filter(
        username=request.user.username)}
    return render(request, 'students/teacherdashboard.html', context)


def logoutend(request):
    return render(request, 'students/login.html')
