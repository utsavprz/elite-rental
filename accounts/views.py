from django.shortcuts import redirect, render
from django.template import loader
from django.contrib.auth.models import User,auth
# Create your views here.
def register(request):
    context={

    }

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                print('Username Already Taken')
            elif User.objects.filter(email=email).exists():
                print('Email Already Taken')
            user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
            user.save();
            print('user created')
        else:
            print("Password not match")
        return redirect('login.htm')
    else:
        return render(request, "accounts/register.htm",context)

def login(request):
    context={

    }
    return render(request, "accounts/login.htm",context)