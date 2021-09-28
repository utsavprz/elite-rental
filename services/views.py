from django.contrib.auth import login
from services.models import Category, bookInstantly, vehicleInfo, vehicleReview, callBack, paymentGateway
from typing import ContextManager
from django.shortcuts import redirect, render
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
    review_count =  vehicleReview.objects.filter(car_id_id = car_id).count()

    if request.method=='POST' and 'SendReview' in request.POST:
        name = request.POST.get('fullname')
        email = request.POST.get('email')
        message = request.POST.get('message')
        car_id_id = car_pk.id

        if name and email and message != '':
            review = vehicleReview(name=name, email=email, message=message, car_id_id=car_id_id)
            review.save()
            print(f"The review has been posted")
            return redirect('contact:success')

    if request.method=='POST' and 'BookInstantly' in request.POST:

        current_user = request.user

        name = request.POST.get('name')
        email = request.POST.get('email')
        number = request.POST.get('phone')
        pickAddress = request.POST.get('pickupAddress')
        pickDate = request.POST.get('pickupDate')
        pickTime = request.POST.get('pickupTime')
        dropAddress = request.POST.get('dropAddress')
        dropDate = request.POST.get('dropDate')
        dropTime = request.POST.get('dropTime')
        car_id_id = car_pk.id
        user_id_id = current_user.id

        if name and email and number != '':
            book = bookInstantly(name=name, email=email, number=number, 
            pickAddress=pickAddress, pickDate=pickDate, pickTime=pickTime, 
            dropAddress=dropAddress, dropDate=dropDate, dropTime=dropTime, 
            car_id_id=car_id_id, user_id_id=user_id_id)

            book.save()
            print(f"Booking has been processed")

            paymentGateway(book_id = bookInstantly.objects.latest('id').id, car_id = car_pk.id, user_id = current_user.id).save()
            print(f"Payment has been set to unpaid")
            return redirect('services:payment')
            
            

            
    
    if request.method=='POST' and 'Callback' in request.POST:

        current_user = request.user
        name = request.POST.get('name')
        email = request.POST.get('email')
        number = request.POST.get('phone')
        pickAddress = request.POST.get('pickupAddress')
        pickDate = request.POST.get('pickupDate')
        pickTime = request.POST.get('pickupTime')
        dropAddress = request.POST.get('dropAddress')
        dropDate = request.POST.get('dropDate')
        dropTime = request.POST.get('dropTime')
        car_id_id = car_pk.id
        user_id_id = current_user.id

        if name and email and number != '':
            callback = callBack(name=name, email=email, number=number, 
            pickAddress=pickAddress, pickDate=pickDate, pickTime=pickTime, 
            dropAddress=dropAddress, dropDate=dropDate, dropTime=dropTime, 
            car_id_id=car_id_id, user_id_id=user_id_id)

            callback.save()
            print(f"Callback has been processed")
    


    review_car = vehicleReview.objects.filter(car_id_id = car_id).order_by('timeStamp')

    context ={
        'car_pk':car_pk,
        'review_car': review_car,
        'review_count': review_count,
    }
    return render(request, 'services/detail.html',context)

def booking(request):
    current_user = request.user
    history = bookInstantly.objects.filter(user_id_id = current_user.id)
    img = vehicleInfo.objects.all()


    context ={
        'history': history,
        'img':img,
        
    }
    return render(request,'services/book.html',context)


def payment(request):
    current_user = request.user

    payment_info = paymentGateway.objects.filter(user_id = current_user.id).latest('id')
    info = vehicleInfo.objects.all()


    context ={
        'payment_info':payment_info,
        'info':info,
        'current_user':current_user.username,
        
    }
    return render(request,'services/payment.html',context)

