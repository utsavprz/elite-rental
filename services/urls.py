from django.urls import path


from . import views

app_name='services'

urlpatterns = [
    path("", views.index, name="index"),
    path("cars", views.display, name="display"),
    path('detail/<int:car_id>', views.detail, name="detail"),
    path('booking', views.booking, name="booking"),
    path('payment', views.payment, name="payment"),
]