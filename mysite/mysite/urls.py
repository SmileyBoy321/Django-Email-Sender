from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("EmailSender/", include("EmailSender.urls")),
    path('admin/', admin.site.urls),
]
