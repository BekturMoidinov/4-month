from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from user.forms import RegisterForm, LoginForm,SMScodeForm
from django.contrib.auth.decorators import login_required
from user.models import Profile,SMScode
import random
# Create your views here.

def register_view(request):
    if request.method == 'GET':
        form=RegisterForm()
        return render(request, 'user/register.html',{'form':form})
    elif request.method == 'POST':
        form=RegisterForm(request.POST,request.FILES)
        if form.is_valid() is False:
            return render(request, 'user/register.html',{'form':form})

        user=User.objects.create_user(
            username=form.cleaned_data['username'],
            first_name=form.cleaned_data['first_name'],
            last_name=form.cleaned_data['last_name'],
            email=form.cleaned_data['email'],
            password=form.cleaned_data['password'],
            is_active=False
        )
        Profile.objects.create(
            user=user,
            age=form.cleaned_data['age'],
            avatar=form.cleaned_data['avatar'],
            bio=form.cleaned_data['bio']
        )
        SMScode.objects.create(
            user=user,
            code= str(random.randint(1000,9999))
        )
        return redirect('confirm')

def login_view(request):
    if request.method == 'GET':
        form=LoginForm()
        return render(request, 'user/login.html',{'form':form})
    elif request.method == 'POST':
        form=LoginForm(request.POST)
        if form.is_valid() is False:
            return render(request, 'user/login.html',{'form':form})
        user = authenticate(**form.cleaned_data)

        if user is False:
            form.add_error(None,'Invalid username or password')
            return render(request, 'user/login.html',{'form':form})

        login(request, user)
        return redirect('home')
@login_required(login_url='/login/')
def profile_view(request):
    if request.method == 'GET':
        return render(request, 'user/profile.html')

@login_required(login_url='/login/')
def logout_view(request):
    logout(request)
    return redirect('home')

def confirmation_view(request):
    if request.method == 'GET':
        form= SMScodeForm()
        return render(request, 'user/confirmation.html',{'form':form})
    elif request.method == 'POST':
        form = SMScodeForm(request.POST)
        if form.is_valid() is False:
            return render(request, 'user/confirmation.html',{'form':form})
        code = form.cleaned_data['code']
        sms_code= SMScode.objects.filter(code=code).first()

        if sms_code is None:
            form.add_error(None,'Invalid code')
            return render(request, 'user/confirmation.html',{'form':form})

        sms_code.user.is_active = True
        sms_code.user.save()
        sms_code.delete()

        return redirect('home')
