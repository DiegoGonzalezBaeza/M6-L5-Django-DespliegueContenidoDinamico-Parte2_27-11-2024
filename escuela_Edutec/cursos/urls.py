from django.urls import path
from . import views

urlpatterns = [
    # es '' por que ya se definio en urls del proyecto
    path('', views.lista_cursos, name='lista_cursos'),
]