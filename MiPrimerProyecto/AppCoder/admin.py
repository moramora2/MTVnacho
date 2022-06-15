from django.contrib import admin

from AppCoder.models import Familia
# Register your models here.

class FamiliaAdmin(admin.ModelAdmin):
    
    list_display = ("id_familia", "nombre", "apellido", "edad", "fecha")
    
admin.site.register(Familia, FamiliaAdmin)
