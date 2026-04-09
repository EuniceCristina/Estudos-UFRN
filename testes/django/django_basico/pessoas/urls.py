from django.urls import path
from . import views


app_name = "pessoas"
urlpatterns = [
    path("",views.user_login, name="user_login"),
    path("user_create",views.user_create, name="user_create"),
    path("inserir_user",views.inserir_user, name="inserir_user"),
]

