from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings
from django.shortcuts import render
from apps.provider_lister.product import product, product_service

def index(request):
    product_service.Product_Service.clear_products()
    for provider in settings.PROVIDERS:
        product_service.Product_Service.add_products(provider.fetch_offers())
        context = {
                "products": product_service.Product_Service.get_products()
                }
        return render(request, "product_list.html", context)
