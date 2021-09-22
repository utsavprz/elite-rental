from django.shortcuts import render


# Create your views here.

def index(request):
    context={

    }
    return render(request,'home/index.html',context)

def error_404(request,exception):
    return render(request, 'home/error.html')