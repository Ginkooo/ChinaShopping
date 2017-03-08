from django.conf.urls import url
from django.contrib import admin
import apps.provider_lister.views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', apps.provider_lister.views.index)
]
