from django.shortcuts import render
# View que apensa renderiza uma página Web
from django.views.generic import TemplateView
# Create your views here.


# Cria uma view para renderizar a pagina inicial
# e faz uma herança de TemplateView
class PaginaInicial(TemplateView):
    template_name = "paginasweb/index.html"