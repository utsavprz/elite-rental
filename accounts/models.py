
from django.db import models
from django.conf import settings

# Create your models here.

class UserAddress(models.Model):
    country_choices=(
    ("Nepal","Nepal"),
    )

    user_info= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)   
    address = models.CharField(max_length=150)
    street = models.CharField(max_length=150)
    postalcode = models.CharField(max_length=10)
    city = models.CharField(max_length=150)
    country = models.CharField(max_length=150, choices=country_choices, default='Nepal')
    
    def __str__(self):
        return f'{self.user_info.id} -- {self.user_info.first_name} {self.user_info.last_name} -- {self.user_info.email}'
    

