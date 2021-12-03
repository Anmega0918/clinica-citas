from rest_framework import viewsets
from .serializer import *
from .models import *

class CitasViewset(viewsets.ModelViewSet):
    queryset = Citas.objects.all()
    serializer_class = CitasSerializer

class PacienteViewset(viewsets.ModelViewSet):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer
