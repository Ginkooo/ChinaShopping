from django.http import HttpResponse
from django.shortcuts import render

import apps.providers.provider_list as provider_list


def index(request):
    product_list = []
    for prov in provider_list.ProviderList.get():
        product_list += prov.fetch_offers()
    context = {"products": product_list}
    return render(request, "product_list.html", context)
