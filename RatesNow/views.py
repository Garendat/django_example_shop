from django.http import HttpResponse
from django.shortcuts import render
from .froms import *
from products.models import ProductImage


# Create your views here.

def index(request):
    context = 'I love you'
    form = SubscriberForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)

        save_form = form.save()

    return render(request, 'RatesNow/index.html', locals())

def home(request):
    product_images = ProductImage.objects.filter(is_active=True, is_main=True)
    product_images_phones = product_images.filter(product__category__id=1)
    product_images_laptops = product_images.filter(product__category__id=2)
    return render(request, 'RatesNow/home.html', locals())
