from django.db import models
from django.conf import settings
from multiselectfield import MultiSelectField

# Create your models here.

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
    ("Apple CarPlay/Android Auto","Apple CarPlay/Android Auto"),
    ("Backup camera","Backup camera"),
    ("Cruise Control","Cruise Control"),
    ("Push-Button Start","Push-Button Start")
    )

    registration_no = models.CharField(max_length=150)
    name = models.CharField(max_length=150)
    price = models.IntegerField()
    cc = models.CharField(max_length=150)
    year = models.CharField(max_length=150)
    category = models.CharField(max_length=150, choices=vehicle_category, default='Sedan')
    color = models.CharField(max_length=150)
    brand = models.CharField(max_length=150)
    transmission = models.CharField(max_length=150, choices=transmission_type, default='Manual')
    passenger = models.CharField(max_length=150, choices=passenger_capacity, default='2')
    bootCapacity = models.CharField(max_length=150)
    carFuel = models.CharField(max_length=150, choices=fuel_type, default='Petrol')
    availability = models.CharField(max_length=150, choices=bool, default='Yes')
    features = MultiSelectField(choices=vehicle_feature, max_choices=9,max_length=150)
    image = models.ImageField(upload_to="services/images")
    addedDate = models.DateField()

    def __str__(self):
        return self.name
    

