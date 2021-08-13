from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:success')
        else:
            messages.error(request, "Error")

    context ={
        'form':form
    }
    return render(request, 'accounts/register.htm',context)

def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,username=username, password=password)

        if username and password != '':
            if user is not None:
                login(request,user)
                return redirect('accounts:success')
            else:
                messages.info(request, "*Username or password is incorrect")
        else:
            messages.info(request, "*Enter username and password")

        context={

        }
    return render(request, "accounts/login.htm")

def success(request): 
    return render(request, "accounts/success.htm")