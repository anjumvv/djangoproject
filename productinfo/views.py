from django.shortcuts import render

# Create your views here.
from django.template import loader
from django.http import HttpResponse,JsonResponse
from .models import product

def displayProduct(request,id):
    template=loader.get_template("product.html")
    prod=product.objects.get (id=id)
    #print(pro)
    data = {"id":prod.id,
            "name":prod.name,
            "desc":prod.desc,
            "price":prod.price}
    res = template.render(data, request)
    return HttpResponse(res)
def myproducts(request):
    template = loader.get_template("myproducts.html")
    products = product.objects.all()
    mydata = {"products": products}
    res = template.render(mydata, request)
    return HttpResponse(res)
def addToCart(request):
    print ("@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    id = request.GET['pid']
    qty = request.GET['qty']

    cartItems = {}

    if request.session.__contains__("cart"):
        cartItems = request.session['cart']

    cartItems[id] = qty
    request.session['cart'] = cartItems
    print(request.session['cart'])
    return HttpResponse("Added Item to Cart")


def viewCart (request):
    template = loader.get_template("cart.html")
    if request.session.__contains__("cart"):
        cartItems = request.session['cart']

        items= []
        for x,y in cartItems.items():
            items.append ( {"id": x, "qty": y})
            p =product.objects.get(id=x)
            items.append ({"id": x,
                            "qty": y,
                            "name": p.name ,
                            "price": p.price,
                            "total" : p.price * int(y)
                            })

        data ={"products": items}
        for x,y in cartItems.items():
            items.append ( {"id": x, "qty": y})

        data ={"products": items}

        res = template.render(data, request)
        return HttpResponse(res)
    else :
        return HttpResponse("Your Cart is Empty")

def writeCookie(req):

    res = HttpResponse("Testing")
    res.set_cookie("TEST_COOKIE", "VIJEESH")
    res.set_cookie("TEST_EMAIL", "vijeesh.tp@expertzlab.com")
    return res;

def readCookie(req):

    val = req.COOKIES['TEST_EMAIL']
    res = HttpResponse(val)
    return res
def getDataPage(req):
    template = loader.get_template("data.html")
    res = template.render({}, req)
    return HttpResponse(res)


def getData (request):

    products= ["OPPO", "VIVO", "Samsung"]
    prices= [1000,20000,30000]
    data = {
        "products": products,
        "prices": prices
    }
    return JsonResponse(data)