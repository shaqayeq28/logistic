from django.urls import path

from car.views import CarView, CarDetailView

urlpatterns = [
    path('car/', CarView.as_view(), name="car"),
    path('car/<int:pk>', CarDetailView.as_view(), name="car_detail"),

]