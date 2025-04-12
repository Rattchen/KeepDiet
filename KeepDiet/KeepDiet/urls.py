from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("", include('tracker.urls')),
    path("vantry/", include('vantry.urls')),
    path("user/", include('accounts.urls')),
    path("admin/", admin.site.urls),
]
