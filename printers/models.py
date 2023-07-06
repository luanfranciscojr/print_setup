from django.db import models


# Create your models here.
class Printer(models.Model):
    name = models.CharField(max_length=255)
    ip = models.CharField(max_length=255)
    port = models.IntegerField(blank=False, null=False)

    def __str__(self) -> str:
        return self.name
    

class Template(models.Model):
    name = models.CharField(max_length=255)
    template = models.TextField()

    def __str__(self) -> str: 
        return self.name
    