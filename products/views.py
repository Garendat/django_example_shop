from django.http import HttpResponse
from django.shortcuts import render
from .froms import *


def product(request, product_id):
    products = Product.objects.get(id=product_id)

    session_key = request.session.session_key

    if not session_key:
        request.session.cycle_key()
    print(request.session.session_key)

    return render(request, 'products/product.html', locals())