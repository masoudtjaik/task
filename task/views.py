from django.shortcuts import render,redirect
from  .forms import DutiesForm,UserForm,SearchForm
from .models import *
from django.db.models import Q
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.models import User
from django.contrib import messages
from .random_test import GetRandom
# Create your views here.

def home(request):
    username=request.session.get('username')
    # print(request.session['user']['username'])
    if username== 'masoudtj':
        task=Task.objects.select_related('category').order_by('-id')
    else:
        task=Task.objects.select_related('category').filter(user__username__exact=username).order_by('-id')
    # task=Task.objects.select_related('category')
    contex={
        'tasks':task,
    }
    if request.method == 'POST':
        forms=SearchForm(request.POST)
        if forms.is_valid():
            search=forms.cleaned_data['search']
            search_task=task.filter(
               Q(title__icontains=search)|Q(category__title__icontains=search))
            # | Q(task_category__title__icontains=search)|
            #      Q(description__icontains=search)  
            if search_task:
                 contex['tasks']=search_task
            else:
                contex['tasks']=''
        contex['forms']=forms
        
    else:
        forms=SearchForm()
        contex['forms']=forms
    response =render(request,'duties/home.html',contex)
    # print(request.session['username'])
    # is_true=request.COOKIES.get('logind')
    # if is_true:
    #     contex['login']='welcome '+request.COOKIES['username']
    # request.session['username'] = 'mini'
    # response.set_cookie('username','masoudtj')
    # response.set_cookie('logind',True)
    # response.delete_cookie('username')
    return response

def login_page (request):
    # x,y=GetRandom.get_random(),GetRandom.get_random()
    if request.method=='POST':
        forms=UserForm(request.POST)
        if forms.is_valid():
            list_forms=forms.cleaned_data
            user=authenticate(request,username=list_forms['username'],password=list_forms['password'])
            if user :
                login(request,user)
                # messages.success(request,'Login done ','success')
                request.session['username']=list_forms['username']
                return redirect('task:home')
            else:
                messages.success(request,'username or password is wrong ','danger')
   
    forms=UserForm()
        # forms.clean_random
        # print('hello')
        
    context={
        'forms':forms
    }
    return render(request,'duties/login.html',context)
x,y=0,0
def login_page2 (request):
    global x
    global y
    if request.method=='POST':
        forms=UserForm(request.POST)
        if forms.is_valid():
            list_forms=forms.cleaned_data
            user=authenticate(request,username=list_forms['username'],password=list_forms['password'])
            if user :
                if list_forms['random']== (x+y):
                    login(request,user)
                    # messages.success(request,'Login done ','success')
                    request.session['username']=list_forms['username']
                    return redirect('task:home')
                else:
                    messages.success(request,'number is wrong ','danger')
                    return redirect('task:login')
            else:
                messages.success(request,'username or password is wrong ','danger')
                
                
    else:
        forms=UserForm()
        # forms.clean_random
        x,y=GetRandom.get_random(),GetRandom.get_random()
        
    context={
        'forms':forms,
        'x':x,
        'y':y
    }
    return render(request,'duties/login2.html',context)

def logout_page(request):
    logout(request)
    # messages.success(request,'Logout done ','success')
    
    return redirect('task:home')

def detail(request,id):
    task = Task.objects.get(pk=id)
    context={
        'task':task
    }
    return render(request,'duties/detail.html',context)

def detail_submits(request,id):
    if request.method=='POST':
        if 'back' in request.POST:
            return redirect('task:home')
        elif 'done' in request.POST:
            task=Task.objects.get(pk=id)
            task.dlt=1
            task.save()
            return redirect('task:home')