from django.db import models
from django.db.models import F, Q, When
from django.conf import settings
from django.db.models.fields import DateTimeField
from multiselectfield import MultiSelectField

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class vehicleInfo(models.Model):
    vehicle_category=(
    ("Sedan","Sedan"),
    ("SUV","SUV"),
    ("4Wheel","4Wheel"),
    ("Electric","Electric"),
    ("Pick-up","Pick-up"),
    ("Vans","Vans"),
    )

    transmission_type=(
    ("Manual","Manual"),
    ("Automatic","Automatic"),
    ("CVT","CVT"),
    )

    passenger_capacity=(
    ("2","2"),
    ("4","4"),
    ("5","5"),
    ("7","7"),
    ("15","15"),
    )
    fuel_type=(
    ("Petrol","Petrol"),
    ("Diesel","Diesel"),
    ("Electric","Electric"),
    )

    bool=(
    ("Yes","Yes"),
    ("No","No"),
    )

    vehicle_feature=(
    ("Sunroof","Sunroof"),
    ("GPS","GPS"),
    ("All Wheel drive","All Wheel drive"),
    ("Heated seats","Heated seats"),
    ("Bluetooth","Bluetooth"),
    ("Apple CarPlay","Apple CarPlay"),
    ("Android Auto","Android Auto"),
    ("Backup camera","Backup camera"),
    ("Cruise Control","Cruise Control"),
    ("Push-Button Start","Push-Button Start")
    )

    registration_no = models.CharField(max_length=150)
    name = models.CharField(max_length=150)
    price = models.IntegerField()
    cc = models.CharField(max_length=150)
    year = models.CharField(max_length=150)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    color = models.CharField(max_length=150)
    brand = models.CharField(max_length=150)
    transmission = models.CharField(max_length=150, choices=transmission_type, default='Manual')
    passenger = models.CharField(max_length=150, choices=passenger_capacity, default='2')
    bootCapacity = models.CharField(max_length=150)
    carFuel = models.CharField(max_length=150, choices=fuel_type, default='Petrol')
    availability = models.CharField(max_length=150, choices=bool, default='Yes')
    features = MultiSelectField(choices=vehicle_feature, max_choices=10,max_length=150)
    vehicleImage = models.ImageField(upload_to="services/images")
    addedDate = models.DateField()

    
    def __str__(self):
        return f'{self.name} - (Available: {self.availability})'

class vehicleReview(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=100)
    message = models.TextField()
    car_id = models.ForeignKey(vehicleInfo, on_delete=models.CASCADE)
    timeStamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return f'{self.name} - {self.car_id.name}'

class bookInstantly(models.Model):
    st=(
    ("Processing","Processing"),
    ("Booked","Booked"),
    ("Cancelled","Cancelled"),
    ("Done","Done"),
    )

    name = models.CharField(max_length=255)
    email = models.CharField(max_length=100)
    number = models.CharField(max_length=10)
    pickAddress = models.CharField(max_length=255)
    pickDate = models.DateField()
    pickTime = models.TimeField()
    dropAddress = models.CharField(max_length=255)
    dropDate = models.DateField()
    dropTime = models.TimeField()
    status = models.CharField(max_length=150, choices=st, default='Processing')
    car_id = models.ForeignKey(vehicleInfo, on_delete=models.CASCADE)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) 

    def __str__(self):
        return f'{self.id} - {self.status}'

    @property
    def is_done(self):
        bookInstantly.objects.filter(DateTimeField.now > self.dropDate).update(status="Done")

    def is_available(self):
        if self.status == "Done":
            vehicleInfo.objects.get(id = self.car_id).update(availability = "Yes")
            print("availability changed to Yes")
        

class callBack(models.Model):
    st=(
    ("Not Called","Not Called"),
    ("Called","Called"),
    )

    name = models.CharField(max_length=255)
    email = models.CharField(max_length=100)
    number = models.CharField(max_length=10)
    pickAddress = models.CharField(max_length=255)
    pickDate = models.DateField()
    pickTime = models.TimeField()
    dropAddress = models.CharField(max_length=255)
    dropDate = models.DateField()
    dropTime = models.TimeField()
    status = models.CharField(max_length=150, choices=st, default='Processing')
    car_id = models.ForeignKey(vehicleInfo, on_delete=models.CASCADE)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) 

    booked_vehicles = bookInstantly.objects.filter(status = "Booked")
    v_info = vehicleInfo.objects.all()

    

    def __str__(self):
        return f'{self.name} - {self.number} - {self.status} - {self.car_id.name} - {self.car_id.availability}'

class paymentGateway(models.Model):
    st=(
    ("Paid","Paid"),
    ("Unpaid","Unpaid"),
    )
    status = models.CharField(max_length=150, choices=st, default='Unpaid')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) 
    car = models.ForeignKey(vehicleInfo, on_delete=models.CASCADE)
    book = models.ForeignKey(bookInstantly, on_delete=models.CASCADE)

    def __str__(self):
        return f'(Booking ID - {self.book.id}) - {self.user} - {self.car.name} - {self.car.availability} - {self.status} - {self.book.status} '
    