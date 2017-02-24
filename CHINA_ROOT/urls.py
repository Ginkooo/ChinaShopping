from django.conf.urls import url
from django.contrib import admin
import apps.shopper.views as views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', views.index)
]
