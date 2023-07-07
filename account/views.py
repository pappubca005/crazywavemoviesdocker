from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm

def register_fun(request):
    message = ''
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        regstr_form = register_form(request.POST)
        if user_form.is_valid() and regstr_form.is_valid():
            users = user_form.save()
            print('only user is saved...')
            rg = regstr_form.save(commit=False)
            rg.user = users
            regstr_form.save()
            print('Registration Success...')
            login(request, users)
            return redirect('/')
        else:
            print('email already exist...')
            context = {
                'msg': 'Email Already Exist...'
            }
            return render(request, 'account/register.html', context)
    else:
        user_form = UserCreationForm()
        regstr_form = register_form()

    context = {
        'form1': user_form,
        'form2': regstr_form,
    }
    return render(request, 'account/register.html', context)

def login_fun(request):
    if request.method == 'POST':
        form1 = AuthenticationForm(data=request.POST)
        u = form1.get_user()
        if form1.is_valid():
            print('form is valid...')
            users = form1.get_user()
            login(request, users)
            return redirect('/')
        else:
            print('Email Or Password Is Incorrect...')
            context = {
                'msg': 'Email Or Password Is Incorrect...'
            }
            return render(request, 'account/login.html', context)
    else:
        form1 = AuthenticationForm()
    context = {
        'form1': form1,
        'user': request.user
    }
    return render(request, 'account/login.html', context)


