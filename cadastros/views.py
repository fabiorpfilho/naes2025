from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from django.urls import reverse_lazy

from .models import Categoria, SubCategoria, Produto, Usuario, Pedido, ItemPedido

class CategoriaCreate(CreateView):
    template_name = "cadastros/form.html"
    model = Categoria
    success_url = reverse_lazy("index")
    fields = ["nome", "descricao"]
    extra_context = {
        "titulo" : "Cadastro de Categoria"
    }
    
class SubCategoriaCreate(CreateView):
    template_name = "cadastros/form.html"
    model = SubCategoria
    success_url = reverse_lazy("index")
    fields = ["nome", "descricao", "categoria"]
    extra_context = {
        "titulo" : "Cadastro de SubCategoria"
    }  
    

class ProdutoCreate(CreateView):
    template_name = "cadastros/form.html"
    model = Produto
    success_url = reverse_lazy("index")
    fields = ["nome", "descricao", "preco", "estoque", "sub_categoria"]
    extra_context = {
        "titulo": "Cadastro de Produto"
    }


class UsuarioCreate(CreateView):
    template_name = "cadastros/form.html"
    model = Usuario
    success_url = reverse_lazy("index")
    fields = ["nome", "email", "endereco", "telefone", "cpf", "tipo"]
    extra_context = {
        "titulo": "Cadastro de Usuário"
    }

    

class PedidoCreate(CreateView):
    template_name = "cadastros/form.html"
    model = Pedido
    success_url = reverse_lazy("index")
    fields = ["pedido_por", "total"]
    extra_context = {
        "titulo": "Cadastro de Pedido"
    }
    
    


class ItemPedidoCreate(CreateView):
    template_name = "cadastros/form.html"
    model = ItemPedido
    success_url = reverse_lazy("index")
    fields = ["pedido", "produto", "nome_produto", "preco"]
    extra_context = {
        "titulo": "Cadastro de Item de Pedido"
    }
    
class CategoriaUpdate(UpdateView):
    template_name = "cadastros/form.html"
    model = Categoria
    success_url = reverse_lazy("index")
    fields = ["nome", "descricao"]
    extra_context = {
        "titulo" : "Atualizar dados de Categoria"
    } 
    
# class CategoriaList(ListView):
#      template_name = "cadastros/listas/categoria.html"
#     model = Campus