from . import views
from django.urls import path, include

urlpatterns = [
    #Paths del Service
    path('',views.services,name="services"),
]