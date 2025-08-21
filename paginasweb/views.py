from django.shortcuts import render
from django.db.models import Sum

# View que apenas renderiza uma página Web
from django.views.generic import TemplateView

from cadastros.models import Produto, Pedido


# Create your views here.

# Cria uma view para renderizar a página inicial
# e faz uma herança de TemplateView
class PaginaInicial(TemplateView):
    template_name = "paginasweb/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #Enviando uma string básica
        context["nome"] = "Fabio Roberto"
        #Enviar uma lista de objetos
        context["ultimos_produtos"] = Produto.objects.all().order_by("nome")[:7]
        context["qtde_produto"] = Produto.objects.all().count()
        context["qtde_pedido"] = Pedido.objects.all().count()
        context["vr_total"] = Pedido.objects.aggregate(Sum("total"))["total__sum"]
        return context


class SobreView(TemplateView):
    template_name = "paginasweb/sobre.html"