from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from django.urls import reverse_lazy

from .models import Categoria

class CategoriaCreate(CreateView):
    template_name = "cadastros/form.html"
    model = Categoria
    success_url = reverse_lazy("index")
    fields = ["nome", "descricao"]
    extra_context = {
        "titulo" : "Cadastro de Categoria"
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