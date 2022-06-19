from django.urls import path

from reception.views import CarCreateView,CarUpdate

urlpatterns = [
    path('reception/', CarCreateView.as_view(), name="reception"),
    path('reception/<int:pk>', CarUpdate.as_view(), name="reception"),

]