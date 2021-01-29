from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
import bcrypt
from datetime import datetime, timedelta, date
from .models import User
from .hfunctions import *

# Create your views here.


def dispLogReg(request):
    return render(request, 'logReg.html')

# Registeration Submit method:
def registerSubmit(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors)>0:
        for key,value in errors.items():
            messages.error(request,value)
        return redirect('/')
    firstName = request.POST['fName']
    lastName = request.POST['lName']
    email = request.POST['eMailr']
    passWord = request.POST['pWordr']
    cryptPass = bcrypt.hashpw(passWord.encode(), bcrypt.gensalt()).decode()
    cKpassWord = request.POST['chkPword']
    confirmKey = createHash()
    newUser = User.objects.create(
        fName=firstName,
        lName=lastName,
        email=email,
        password=cryptPass,
        accessLevel=0,
        active=False,
        confirmKey=confirmKey,
        confirmed=False
    )
    return redirect('/registered')

def success(request):
    return render(request,'success.html')

# registration methond is going to need an emailer method.

def displayAdminPage(request):
    context = {
        'users': User.objects.all()
    }
    return render(request, 'admin.html', context)




# AJAX METHODS-------------------------------------
# =================================================
def dispUsers(request):
    print('made it')
    context = {
        'users':User.objects.all()
    }
    return render(request, 'userSnip.html', context)