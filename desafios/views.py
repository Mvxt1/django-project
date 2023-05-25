from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

desafios_mensais = { 
    "janeiro": "Comer",
    "feveiro": "jantar",
    "marco": "correr",
    "abril": "null",
    "maio": "Django",
    "junho" : None
}
 
# Create your views here.


def index(request):
    mese = list(desafios_mensais.keys())
    return render(request, "desafios/desafio.html", {
        "meses": mese
    })


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
        return render(request, "desafios/mes.html", {
            "text": texto_desafio,
            "mes": mes,
        })
    except:
        return HttpResponseNotFound("Mes nao existe")
