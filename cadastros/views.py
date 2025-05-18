from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

from django.urls import reverse_lazy

from .models import Categoria, SubCategoria, Produto, Usuario, Pedido, ItemPedido

class CategoriaCreate(CreateView):
    template_name = "cadastros/form.html"
    model = Categoria
    success_url = reverse_lazy("listar-categoria")
    fields = ["nome", "descricao"]
    extra_context = {
        "titulo" : "Cadastro de Categoria"
    }
    
class SubCategoriaCreate(CreateView):
    template_name = "cadastros/form.html"
    model = SubCategoria
    success_url = reverse_lazy("listar-sub-categoria")
    fields = ["nome", "descricao", "categoria"]
    extra_context = {
        "titulo" : "Cadastro de SubCategoria"
    }  
    

class ProdutoCreate(CreateView):
    template_name = "cadastros/form.html"
    model = Produto
    success_url = reverse_lazy("listar-produto")
    fields = ["nome", "descricao", "preco", "estoque", "sub_categoria"]
    extra_context = {
        "titulo": "Cadastro de Produto"
    }


class UsuarioCreate(CreateView):
    template_name = "cadastros/form.html"
    model = Usuario
    success_url = reverse_lazy("listar-usuario")
    fields = ["nome", "email", "endereco", "telefone", "cpf", "tipo"]
    extra_context = {
        "titulo": "Cadastro de Usuário"
    }

    def form_valid(self, form):
        # Cria um novo User
        username = form.cleaned_data['email']  # Ou outro campo único
        # Adicione password ao formulário
        password = form.cleaned_data.get('password', 'default_password')
        user = User.objects.create(
            username=username,
            email=form.cleaned_data['email'],
            password=make_password(password)
        )
        # Associa o novo User ao campo usuario
        form.instance.usuario = user
        return super().form_valid(form)

    

class PedidoCreate(CreateView):
    template_name = "cadastros/form.html"
    model = Pedido
    success_url = reverse_lazy("listar-pedido")
    fields = ["pedido_por", "total"]
    extra_context = {
        "titulo": "Cadastro de Pedido"
    }
    

class ItemPedidoCreate(CreateView):
    template_name = "cadastros/form.html"
    model = ItemPedido
    success_url = reverse_lazy("listar-item-pedido")
    fields = ["pedido", "produto", "nome_produto", "quantidade","preco"]
    extra_context = {
        "titulo": "Cadastro de Item de Pedido"
    }
    
###############################################################
    
class CategoriaUpdate(UpdateView):
    template_name = "cadastros/form.html"
    model = Categoria
    success_url = reverse_lazy("listar-categoria")
    fields = ["nome", "descricao"]
    extra_context = {
        "titulo" : "Atualizar dados de Categoria"
    } 
    
    
class SubCategoriaUpdate(UpdateView):
    template_name = "cadastros/form.html"
    model = SubCategoria
    success_url = reverse_lazy("listar-sub-categoria")
    fields = ["nome", "descricao", "categoria"]
    extra_context = {
        "titulo": "Atualizar dados de SubCategoria"
    }


class ProdutoUpdate(UpdateView):
    template_name = "cadastros/form.html"
    model = Produto
    success_url = reverse_lazy("listar-produto")
    fields = ["nome", "descricao", "preco", "estoque", "sub_categoria"]
    extra_context = {
        "titulo": "Atualizar dados de Produto"
    }


class UsuarioUpdate(UpdateView):
    template_name = "cadastros/form.html"
    model = Usuario
    success_url = reverse_lazy("listar-usuario")
    fields = ["nome", "email", "endereco", "telefone", "cpf", "tipo"]
    extra_context = {
        "titulo": "Atualizar dados de Usuário"
    }


class PedidoUpdate(UpdateView):
    template_name = "cadastros/form.html"
    model = Pedido
    success_url = reverse_lazy("listar-pedido")
    fields = ["pedido_por", "total"]
    extra_context = {
        "titulo": "Atualizar dados de Pedido"
    }


class ItemPedidoUpdate(UpdateView):
    template_name = "cadastros/form.html"
    model = ItemPedido
    success_url = reverse_lazy("listar-item-pedido")
    fields = ["pedido", "produto", "nome_produto", "quantidade", "preco"]
    extra_context = {
        "titulo": "Atualizar dados de Item de Pedido"
    }
    
###############################################################


class CategoriaDelete(DeleteView):
    template_name = "cadastros/form-excluir.html"
    model = Categoria
    success_url = reverse_lazy("listar-categoria")
    extra_context = {
        "titulo": "Excluir Categoria"
    }


class SubCategoriaDelete(DeleteView):
    template_name = "cadastros/form-excluir.html"
    model = SubCategoria
    success_url = reverse_lazy("listar-sub-categoria")
    extra_context = {
        "titulo": "Excluir Sub Categoria"
    }


class ProdutoDelete(DeleteView):
    template_name = "cadastros/form-excluir.html"
    model = Produto
    success_url = reverse_lazy("listar-produto")
    extra_context = {
        "titulo": "Excluir Produto"
    }


class UsuarioDelete(DeleteView):
    template_name = "cadastros/form-excluir.html"
    model = Usuario
    success_url = reverse_lazy("listar-usuario")
    extra_context = {
        "titulo": "Excluir Usuário"
    }


class PedidoDelete(DeleteView):
    template_name = "cadastros/form-excluir.html"
    model = Pedido
    success_url = reverse_lazy("listar-pedido")
    extra_context = {
        "titulo": "Excluir Pedido"
    }


class ItemPedidoDelete(DeleteView):
    template_name = "cadastros/form-excluir.html"
    model = ItemPedido
    success_url = reverse_lazy("listar-item-pedido")
    extra_context = {
        "titulo": "Excluir Item do Pedido"
    }
    

###############################################################


class CategoriaList(ListView):
    template_name = "cadastros/listas/categoria.html"
    model = Categoria


class SubCategoriaList(ListView):
    template_name = "cadastros/listas/subCategoria.html"
    model = SubCategoria


class ProdutoList(ListView):
    template_name = "cadastros/listas/produto.html"
    model = Produto


class UsuarioList(ListView):
    template_name = "cadastros/listas/usuario.html"
    model = Usuario

class PedidoList(ListView):
    template_name = "cadastros/listas/pedido.html"
    model = Pedido


class ItemPedidoList(ListView):
    template_name = "cadastros/listas/itemPedido.html"
    model = ItemPedido
    
    
# class CategoriaList(ListView):
#      template_name = "cadastros/listas/categoria.html"
#     model = Campus