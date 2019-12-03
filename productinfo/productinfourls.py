from django.urls import path,include
from .views import displayProduct, myproducts, addToCart, viewCart
from .views import displayProduct, myproducts, addToCart, viewCart,writeCookie,readCookie,getData,getDataPage
from .classview import MyView
urlpatterns = [
    path('product/<str:id>', displayProduct),
    path('myproducts',myproducts),
    #path('products', myProducts),
    path('addToCart', addToCart),
    path('viewCart', viewCart),
    path ('viewCart', viewCart),
    path('writeCookie', writeCookie),
    path('readCookie', readCookie),
    path ('myview', MyView.as_view()),
    path('productdata',getData),
    path('data',getDataPage)
]