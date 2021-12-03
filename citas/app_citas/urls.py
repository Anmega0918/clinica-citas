from django.db import router
from rest_framework import routers, urlpatterns
from .viewset import *

router = routers.SimpleRouter()
router.register('',PacienteViewset)
router.register('api/v1.0/citas',CitasViewset)


urlpatterns = router.urls