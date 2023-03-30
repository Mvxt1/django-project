from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

desafios_mensais = {
    "janeiro": "Comer",
    "feveiro": "jantar",
    "marco": "correr",
    "abril": "null",
    "maio": "Django"
}

# Create your views here.


def index(reques):
    response_data = "<ul><li>Meuas</li></ul>"
    return HttpResponse(response_data)

def desafios_number(request, mes):
    mes_numero = list(desafios_mensais.keys())

    if mes > len(mes_numero):
        return HttpResponseNotFound("Mes invalido")

    mes_direcionado = mes_numero[mes-1]
    caminho_reverse = reverse("mes_letra", args=[mes_direcionado])
    return HttpResponseRedirect(caminho_reverse)


def desafios(request, mes):
    try:
        texto_desafio = desafios_mensais[mes]
        return HttpResponse(texto_desafio)
    except:
        return HttpResponseNotFound("Mes nao existe")
