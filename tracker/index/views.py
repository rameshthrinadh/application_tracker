from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import *
from django.contrib.auth import authenticate, login,logout
from django.db.models import F 

# Create your views here.

def add (request):

    if request.method == 'POST':
        application=applications()
        application.sname=request.POST['name']
        application.sid=request.POST['id']
        application.semail=request.POST['email']
        application.type=request.POST['type']
        application.subject=request.POST['subject']
        application.message=request.POST['message']
        application.step=0
        application.save()

    number=application.id
    return render(request,'output.html',{'number': number})


def check (request):

    if request.method == 'POST':
        application=applications()
        number=request.POST['number']
        progress=applications.objects.get(id=number)

    return render(request,'progress.html',{'progress': progress.step, 'type':progress.type})

def process(request):
 
    if request.method == 'POST':
        d =request.POST['processed']
        step=int(request.POST['step'])
        if step < 5:
            progress=applications.objects.filter(id=d).update(step = F('step')+1)
       
    return redirect('dashboard')


def goback(request):

    if request.method == 'POST':
        id =request.POST['goback']
        step=int(request.POST['step'])
        if step >0 :
            progress=applications.objects.filter(id=id).update(step = F('step')-1)
       

   
    return redirect('dashboard')

def index(request):

    return render(request,'index.html', {'nbar' :'index'})

def request(request):

    return render(request,'request.html',{'nbar':'request'})

def dashboard(request):
    if request.user.is_authenticated:
        if request.user.username == 'examcell' :
            application=applications.objects.filter(type='Marks List')
        elif request.user.username == 'administration':
            application=applications.objects.filter(type='Study Certificate')
        return render(request,'dashboard.html',{'application':application, 'nbar':'dashboard','uname':request.user.username})
    else:
        return render(request,'login.html',{'nbar' :'login'})


def logi(request):
    return render(request,'login.html',{'nbar' :'login'})

def auth(request):
      if request.method == 'POST':
        uname= request.POST['username']
        passwd= request.POST['password']
        user =authenticate(request, username=uname, password=passwd)
        if user is not None:
            login(request,user)
            return redirect('dashboard')
        else:
            return render(request,'login.html',{'authenti':'false'})

def user_logout(request):
    logout(request)
    return redirect('logi')

def forward(request):

     if request.method == 'POST':
        id =request.POST['id']
        app_type=request.POST['type']
        if app_type == 'Study' :
            progress=applications.objects.filter(id=id).update(type="Marks List")
        elif app_type == 'Marks':
            progress=applications.objects.filter(id=id).update(type="Study Certificate")
    
     return redirect('dashboard')

def decline(request):
    if request.method == 'POST':
        id =request.POST['id']
        progress=applications.objects.filter(id=id).update(step = -1)
    return redirect('dashboard')
