from django.urls import path
from . import views


urlpatterns = [
    path("ver_user",views.ver_user, name="ver_user"),
    path("inserir_user",views.inserir_user, name="inserir_user"),
]

