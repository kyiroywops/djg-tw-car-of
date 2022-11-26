from django.urls import path
from . import views

from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('nosotros', views.nosotros, name="nosotros"),
    path('autos', views.libros, name="autos"),
    path('autos/crear', views.crear, name="crear"),
    path('autos/editar', views.editar, name="editar"),
    path('eliminar/<int:id>', views.eliminar, name="eliminar"),
    path('autos/editar/<int:id>', views.editar, name="editar"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)