from django.urls import path
from .views import lista_publicaciones, detalle_publicacion, registro, iniciar_sesion, cerrar_sesion, crear_publicacion, agregar_comentario

urlpatterns = [
    path('', lista_publicaciones, name='lista_publicaciones'),
    path('publicacion/<int:id>/', detalle_publicacion, name='detalle_publicacion'),
    path('registro/', registro, name='registro'),
    path('iniciar-sesion/', iniciar_sesion, name='iniciar_sesion'),
    path('cerrar-sesion/', cerrar_sesion, name='cerrar_sesion'),
    path('crear-publicacion/', crear_publicacion, name='crear_publicacion'),
    path('publicacion/<int:id>/comentar/', agregar_comentario, name='agregar_comentario'),
]
