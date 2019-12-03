from django.contrib import admin
from django.urls import path
from .views import home, login, register, contactPage
from .views import home, login, register,contactPage, saveContact
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home',home),
    path('login',login),
    path('register',register),
    path('contact', contactPage),
    path('contact', contactPage),
    path('saveContact', saveContact)
]
