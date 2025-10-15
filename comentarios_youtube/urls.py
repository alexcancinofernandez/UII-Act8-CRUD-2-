from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_comentarios, name='lista_comentarios'),
    path('agregar/', views.agregar_comentario, name='agregar_comentario'),
    path('editar/<str:pk>/', views.editar_comentario, name='editar_comentario'),
    path('eliminar/<str:pk>/', views.eliminar_comentario, name='eliminar_comentario'),
]