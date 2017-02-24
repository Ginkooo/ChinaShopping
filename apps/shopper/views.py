from django.http import HttpResponse
from django.shortcuts import render

import apps.providers.provider as provider


def index(request):
    product_list = []
    for prov in provider.ProviderList.get():
        product_list += prov.fetch_offers()
    context = {"products": product_list}
    return render(request, "product_list.html", context)
