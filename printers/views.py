import socket

from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Printer, Template


class PrinterView(APIView):
    # add permission to check if user is authenticated

    # 2. Create
    def post(self, request, *args, **kwargs):

        template = Template.objects.get(id = request.data.get('templateId'))
        printer = Printer.objects.get(id =request.data.get('printerId'))
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
        s.connect((printer.ip, printer.port))
        s.send(bytes(template.template, "utf-8"))
        s.close()
        return Response("", status=status.HTTP_201_CREATED)

