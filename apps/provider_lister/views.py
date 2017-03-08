from django.http import HttpResponse
from django.shortcuts import render
from django.conf.settings as settings


def index(request):
    product_list = []
    for provider in settings.PROVIDERS:
        product_list.append(provider.fetch_offers())
    print("Offers fetched!")
