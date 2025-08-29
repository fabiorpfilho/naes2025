from django.shortcuts import render
from django.db.models import Sum
from django.views.generic import TemplateView
from cadastros.models import Produto, Pedido, Usuario, TipoUsuario

class PaginaInicial(TemplateView):
    template_name = "paginasweb/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["nome"] = "Fabio Roberto"
        context["ultimos_produtos"] = Produto.objects.all().order_by("nome")[:7]
        context["qtde_produto"] = Produto.objects.all().count()
        context["qtde_pedido"] = Pedido.objects.all().count()
        context["vr_total"] = Pedido.objects.aggregate(Sum("total"))["total__sum"]
        context["qtde_clientes"] = Usuario.objects.filter(tipo=TipoUsuario.CLIENTE).count()
        return context

class SobreView(TemplateView):
    template_name = "paginasweb/sobre.html"