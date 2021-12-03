from django.db import models
from django.utils.safestring import mark_safe

# Create your models here.

def url(self,filename):
    ruta = "static/img/pacientes/%s/%s"%(self.nombre,str(filename))
    return ruta

class Paciente(models.Model):

    def soporte_paciente(self):
        return mark_safe('<a  href="/%s"> <img src="/%s"width=50px height=50px /> </a>'%(self.soporte,self.soporte))

    nombre = models.CharField(max_length=50, blank=False)
    apellido = models.CharField(max_length=50, blank=False)
    telefono = models.IntegerField(blank=False)
    correo = models.EmailField(blank=False)
    direccion = models.CharField(max_length=100,blank=False)
    soporte = models.ImageField(upload_to=url)

    def __str__(self):
        return self.nombre


        
tipo_cita = [ 
    ('URGENCIAS', 'URGENCIAS'),
    ('CONTROL', 'CONTROL'),
    ('PRIORITARIA', 'PRIORITARIA'),
    ('ODONTOLOGICA', 'ODONTOLOGICA'),
    ('ESPECIALISTA','ESPECIALISTA'),
]

horario_cita = [
    ('Mañana1', '7AM'),
    ('Mañana2', '8AM'),
    ('Mañana3', '9AM'),
    ('Mañana4', '10AM'),
    ('Mañana5', '11AM'),
    ('Tarde1', '1PM'),
    ('Tarde2', '2PM'),
    ('Tarde3', '3PM'),
    ('Tarde4', '4PM'),
    ('Tarde5', '5PM'),
]   

class Citas(models.Model):
    cedula = models.IntegerField(blank=False)
    tipocita = models.CharField(max_length=50, choices= tipo_cita,default='available')
    fecha = models.DateField(blank=False)
    horariocita = models.CharField(max_length=50, choices= horario_cita,default='available')
    IDpaciente = models.OneToOneField(Paciente,on_delete=models.CASCADE, blank=False)

    def __str__(self):
        return self.tipocita
