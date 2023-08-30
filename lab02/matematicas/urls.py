from django.urls import path

from . import views

app_name = 'matematicas'

urlpatterns = [
    path('operaciones', views.index, name='index'),
    path('operaciones/enviar', views.enviar, name='enviar'),
    path('volumen', views.index2, name='index2'),
    path('volumen/enviar', views.enviar2, name='enviar2'),
]