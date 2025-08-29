
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django import forms
from .models import ItemPedido, Usuario, Produto, Pedido

class ItemPedidoForm(forms.ModelForm):
    class Meta:
        model = ItemPedido
        fields = ["pedido", "produto", "quantidade"]

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Filtra os pedidos para mostrar apenas os criados pelo usuário logado
        if user and hasattr(user, 'usuario'):
            self.fields['pedido'].queryset = Pedido.objects.filter(pedido_por=user.usuario)
