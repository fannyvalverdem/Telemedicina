from rest_framework import routers
from api import views as myapp_views

router = routers.DefaultRouter()
router.register(r'persona', myapp_views.PersonaViewset)
router.register(r"medico",myapp_views.DoctorViewset)
router.register(r"paquete",myapp_views.PaqueteViewset)
router.register(r"consulta",myapp_views.ConsultaViewset)
router.register(r"especialidad",myapp_views.EspecialidadViewset)


