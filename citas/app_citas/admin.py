from django.contrib import admin
from .models import Paciente, Citas 
# Register your models here.

class PacienteAdmin(admin.ModelAdmin):
    list_display = ('nombre','apellido','telefono','correo','direccion','soporte_paciente')


class CitasAdmin(admin.ModelAdmin):
    list_display = ('cedula', 'IDpaciente','tipocita', 'fecha', 'horariocita')
admin.site.register(Paciente, PacienteAdmin)
admin.site.register(Citas,CitasAdmin)