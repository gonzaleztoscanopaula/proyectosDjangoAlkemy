from django.contrib import admin
from .models import Fabrica, Sucursale, Instrumento
# Register your models here.

class InstrumentoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio','tipo')


admin.site.register(Fabrica)
admin.site.register(Sucursale)
admin.site.register(Instrumento, InstrumentoAdmin)


