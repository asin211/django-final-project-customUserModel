from django.urls import path, include
from customuser import views

urlpatterns = [
    path("", views.home, name='home'),
 
]

