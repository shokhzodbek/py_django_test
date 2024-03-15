from django.shortcuts import render
from .models import Product
# Create your views here.
# ls = [{}]


def index(request):
    products = Product.objects.all()
    context = {
        'products':products
    }
    return render(request,'index.html',context)

def contact(req):
    return render(req,'contact.html')

def shop(req):
    return render(req,'shop.html')

def why(req):
    return render(req,'why.html')

def testmon(req):
    return render(req,'testmonial.html')