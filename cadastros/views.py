from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.shortcuts import get_object_or_404

from django.urls import reverse_lazy

from .models import Categoria, SubCategoria, Produto, Usuario, Pedido, ItemPedido
from .forms import ItemPedidoForm
# View para controle de autenticação e acesso às páginas
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin

class CategoriaCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    group_required = "Administrador"
    login_url = reverse_lazy('login')
    template_name = "cadastros/form.html"
    model = Categoria
    success_url = reverse_lazy("listar-categoria")
    fields = ["nome", "descricao"]
    extra_context = {
        "titulo" : "Cadastro de Categoria"
    }
    
class SubCategoriaCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    group_required = "Administrador"
    login_url = reverse_lazy('login')
    template_name = "cadastros/form.html"
    model = SubCategoria
    success_url = reverse_lazy("listar-sub-categoria")
    fields = ["nome", "descricao", "categoria"]
    extra_context = {
        "titulo" : "Cadastro de SubCategoria"
    }  
    

class ProdutoCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    group_required = "Administrador"
    login_url = reverse_lazy('login')
    template_name = "cadastros/form.html"
    model = Produto
    success_url = reverse_lazy("listar-produto")
    fields = ["nome", "descricao", "preco", "estoque", "sub_categoria"]
    extra_context = {
        "titulo": "Cadastro de Produto"
    }


class UsuarioCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    group_required = "Administrador"
    login_url = reverse_lazy('login')
    template_name = "cadastros/form.html"
    model = Usuario
    success_url = reverse_lazy("listar-usuario")
    fields = ["nome", "endereco", "telefone", "cpf", "tipo"]
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

    

class PedidoCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    template_name = "cadastros/form.html"
    model = Pedido
    success_url = reverse_lazy("listar-pedido")
    fields = ["total"]
    extra_context = {
        "titulo": "Cadastro de Pedido"
    }
    
    def form_valid(self, form):
        # Define o usuário como usuário logado
        form.instance.pedido_por = self.request.user.usuario
        return super().form_valid(form)
    

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import ItemPedido, Usuario, Produto

class ItemPedidoCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    template_name = "cadastros/form.html"
    model = ItemPedido
    form_class = ItemPedidoForm
    success_url = reverse_lazy("listar-item-pedido")
    extra_context = {
        "titulo": "Cadastro de Item de Pedido"
    }
    
    def get_form(self, form_class=None):
        # Passa o usuário logado para o formulário
        if form_class is None:
            form_class = self.form_class
        return form_class(user=self.request.user, **self.get_form_kwargs())
    
    def form_valid(self, form):
        # Define o usuário como usuário logado
        form.instance.pedido_por = self.request.user.usuario
        
        # Obtém o produto selecionado do formulário
        produto = form.cleaned_data['produto']
        
        # Define o nome do produto e o preço com base no objeto Produto
        form.instance.nome_produto = produto.nome
        form.instance.preco = produto.preco
        
        return super().form_valid(form)
    
###############################################################
    
class CategoriaUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    group_required = "Administrador"
    login_url = reverse_lazy('login')
    template_name = "cadastros/form.html"
    model = Categoria
    success_url = reverse_lazy("listar-categoria")
    fields = ["nome", "descricao"]
    extra_context = {
        "titulo" : "Atualizar dados de Categoria"
    } 
    
    
class SubCategoriaUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    group_required = "Administrador"
    login_url = reverse_lazy('login')
    template_name = "cadastros/form.html"
    model = SubCategoria
    success_url = reverse_lazy("listar-sub-categoria")
    fields = ["nome", "descricao", "categoria"]
    extra_context = {
        "titulo": "Atualizar dados de SubCategoria"
    }


class ProdutoUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    group_required = "Administrador"
    login_url = reverse_lazy('login')
    template_name = "cadastros/form.html"
    model = Produto
    success_url = reverse_lazy("listar-produto")
    fields = ["nome", "descricao", "preco", "estoque", "sub_categoria"]
    extra_context = {
        "titulo": "Atualizar dados de Produto"
    }


class UsuarioUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    group_required = "Administrador"
    login_url = reverse_lazy('login')
    template_name = "cadastros/form.html"
    model = Usuario
    success_url = reverse_lazy("listar-usuario")
    fields = ["nome", "email", "endereco", "telefone", "cpf", "tipo"]
    extra_context = {
        "titulo": "Atualizar dados de Usuário"
    }


class PedidoUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    template_name = "cadastros/form.html"
    model = Pedido
    success_url = reverse_lazy("listar-pedido")
    fields = ["pedido_por", "total"]
    extra_context = {
        "titulo": "Atualizar dados de Pedido"
    }
    def get_object(self, queryset=None):
        self.object = get_object_or_404(Pedido, pk=self.kwargs['pk'], pedido_por=self.request.user.usuario)
        return self.object


class ItemPedidoUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    template_name = "cadastros/form.html"
    model = ItemPedido
    success_url = reverse_lazy("listar-item-pedido")
    fields = ["pedido", "produto", "nome_produto", "quantidade", "preco"]
    extra_context = {
        "titulo": "Atualizar dados de Item de Pedido"
    }
    def get_object(self, queryset=None):
        self.object = get_object_or_404(ItemPedido, pk=self.kwargs['pk'], pedido_por=self.request.user.usuario)
        return self.object
    
###############################################################


class CategoriaDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = "Administrador"
    template_name = "cadastros/form-excluir.html"
    model = Categoria
    success_url = reverse_lazy("listar-categoria")
    extra_context = {
        "titulo": "Excluir Categoria"
    }


class SubCategoriaDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    group_required = "Administrador"
    login_url = reverse_lazy('login')
    template_name = "cadastros/form-excluir.html"
    model = SubCategoria
    success_url = reverse_lazy("listar-sub-categoria")
    extra_context = {
        "titulo": "Excluir Sub Categoria"
    }


class ProdutoDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    group_required = "Administrador"
    login_url = reverse_lazy('login')
    template_name = "cadastros/form-excluir.html"
    model = Produto
    success_url = reverse_lazy("listar-produto")
    extra_context = {
        "titulo": "Excluir Produto"
    }


class UsuarioDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    group_required = "Administrador"
    login_url = reverse_lazy('login')
    template_name = "cadastros/form-excluir.html"
    model = Usuario
    success_url = reverse_lazy("listar-usuario")
    extra_context = {
        "titulo": "Excluir Usuário"
    }


class PedidoDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    template_name = "cadastros/form-excluir.html"
    model = Pedido
    success_url = reverse_lazy("listar-pedido")
    extra_context = {
        "titulo": "Excluir Pedido"
    }
    def get_object(self, queryset=None):
        self.object = get_object_or_404(Pedido, pk=self.kwargs['pk'], pedido_por=self.request.user.usuario)
        return self.object


class ItemPedidoDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    template_name = "cadastros/form-excluir.html"
    model = ItemPedido
    success_url = reverse_lazy("listar-item-pedido")
    extra_context = {
        "titulo": "Excluir Item do Pedido"
    }
    def get_object(self, queryset=None):
        self.object = get_object_or_404(ItemPedido, pk=self.kwargs['pk'], pedido_por=self.request.user.usuario)
        return self.object
    

###############################################################


class CategoriaList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    group_required = "Administrador"
    login_url = reverse_lazy('login')
    template_name = "cadastros/listas/categoria.html"
    model = Categoria


class SubCategoriaList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    group_required = "Administrador"
    login_url = reverse_lazy('login')
    template_name = "cadastros/listas/subCategoria.html"
    model = SubCategoria


class ProdutoList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    template_name = "cadastros/listas/produto.html"
    model = Produto


class UsuarioList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    group_required = "Administrador"
    login_url = reverse_lazy('login')
    template_name = "cadastros/listas/usuario.html"
    model = Usuario

class PedidoList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    template_name = "cadastros/listas/pedido.html"
    model = Pedido
    
    def get_queryset(self):
        print("Usuário: ", self.request.user)
        # Verifica se o usuário pertence ao grupo "Administrador"
        if self.request.user.groups.filter(name='Administrador').exists():
            # Para administradores, retorna todos os pedidos
            queryset = Pedido.objects.all()
        else:
            # Para usuários comuns, filtra pedidos pelo usuário logado
            queryset = Pedido.objects.filter(pedido_por=self.request.user.usuario)
        
        return queryset

class ItemPedidoList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    template_name = "cadastros/listas/itemPedido.html"
    model = ItemPedido
    
    def get_queryset(self):
        # O object_list armazena uma lista de objetos de um ListView

        if self.request.user.groups.filter(name='Administrador').exists():
            # Para administradores, retorna todos os pedidos
            queryset = ItemPedido.objects.all()
        else:
            queryset = ItemPedido.objects.filter(pedido_por=self.request.user.usuario)
        return queryset
    
    
    
# class CategoriaList(ListView):
#      template_name = "cadastros/listas/categoria.html"
#     model = Campus