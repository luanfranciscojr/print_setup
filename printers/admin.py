from django.contrib import admin

from .models import Printer, Template


# Register your models here.
class PrintersAdmin(admin.ModelAdmin):
    ...


class TemplateAdmin(admin.ModelAdmin):
    ...


admin.site.register(Printer, PrintersAdmin)
admin.site.register(Template, TemplateAdmin)
  