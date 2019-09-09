from rest_framework import routers
from api import views as myapp_views

router = routers.DefaultRouter()
router.register(r'persona', myapp_views.PersonaViewset)
router.register(r"medico",myapp_views.MedicoViewset)
router.register(r"tarifa",myapp_views.TarifaViewset)
router.register(r"horario",myapp_views.HorarioViewset)
router.register(r"cita",myapp_views.CitaViewset)
router.register(r"receta",myapp_views.RecetaViewset)


