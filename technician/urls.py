from django.urls import path

from technician.views import RepairUpdate,AddPart,RemovePart

urlpatterns = [
    path('technician/<int:pk>', RepairUpdate.as_view(), name="repair"),
    path('technician/part/add/<int:pk>', AddPart.as_view(), name="add_part"),
    path('technician/part/remove/<int:pk>', RemovePart.as_view(), name="remove_part"),

]