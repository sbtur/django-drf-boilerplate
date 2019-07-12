from django.urls import include, path

from core.api import urls

urlpatterns = [
    path("api/", include(urls)),
    path("", include("django.contrib.auth.urls")),
]
