from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from user.forms import RegisterForm, LoginForm
from django.contrib.auth.decorators import login_required
from user.models import Profile
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
            password=form.cleaned_data['password']
        )
        Profile.objects.create(
            user=user,
            age=form.cleaned_data['age'],
            avatar=form.cleaned_data['avatar'],
            bio=form.cleaned_data['bio']
        )
        return redirect('home')

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