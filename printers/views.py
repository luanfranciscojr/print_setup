from django.http import HttpResponse
from django.shortcuts import render

from printers.models import Template


def printers(request):
    return render(request, 'printers.zpl', context={'template': 'teste'})

