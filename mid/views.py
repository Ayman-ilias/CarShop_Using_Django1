from django.shortcuts import render
from carshop.models import Car
from brand.models import Brand

def home(request,catagory_slug=None):
    data = Car.objects.all()
    # catagory=None
    if catagory_slug is not None:
        catagory=Brand.objects.get(slug=catagory_slug)
        data = Car.objects.filter(brand = catagory)
    catagories = Brand.objects.all()
    return render(request,'home.html',{'data' : data, 'catagory': catagories})


