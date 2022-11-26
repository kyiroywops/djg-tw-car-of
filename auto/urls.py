from django.urls import path
from . import views

from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('comision', views.comision, name="comision"),
    path('autos', views.autos, name="autos"),
    path('autos/crear', views.crear, name="crear"),
    path('autos/editar', views.editar, name="editar"),
    path('eliminar/<int:id>', views.eliminar, name="eliminar"),
    path('autos/editar/<int:id>', views.editar, name="editar"),
    path('ventas', views.ventas, name="ventas"),
    path('ventas/crear', views.crearVentas, name="crearVentas"),
    path('ventas/editar', views.editar, name="editarVentas"),
    path('ventas/editar/<int:id>', views.editar, name="editarVentas"),
    path('ventas/eliminar/<int:id>', views.eliminar, name="eliminarVentas"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)