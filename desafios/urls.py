from django.urls import path

from . import views

urlpatterns = [
    path("<int:mes>", views.desafios_number),
    path("<str:mes>", views.desafios, name="mes_letra"),
    path("", views.index)
]
