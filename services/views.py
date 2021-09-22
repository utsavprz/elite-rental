from services.models import Category, vehicleInfo
from typing import ContextManager
from django.shortcuts import render
from django.http import HttpRequest

# Create your views here.

def index(request):
    category = Category.objects.all()

    context = {
        'category':category,
    }

    return render(request,'services/services.html',context)

def display(request):
    
    category = request.GET.get('category')

    category_name = Category.objects.get(id=category)

    vehicle_info = vehicleInfo.objects.all()

    if category != None:
        vehicle_info = vehicleInfo.objects.filter(category = category)


    context = {
        'vehicle_info':vehicle_info,
        'category_name': category_name,
    }
    return render(request,'services/display.html',context) 


def detail(request,car_id):
    car_pk = vehicleInfo.objects.get(pk=car_id)

    context ={
        'car_pk':car_pk
    }
    return render(request, 'services/detail.html',context)