from django.urls import path

from inspector.views import IsFinished

urlpatterns = [
    path('inspector/<int:pk>', IsFinished.as_view(), name="inspector"),


]