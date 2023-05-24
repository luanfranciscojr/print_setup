from django.urls import path

from printers.views import printers

urlpatterns = [
    path('printers/', printers),
]
