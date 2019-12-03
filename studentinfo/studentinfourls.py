from django.urls import path,include
from .views import displayinformation, studentdetails
urlpatterns = [
    path('studentinformation/<int:rrr>', displayinformation),
    path('studentdetails',studentdetails)
]