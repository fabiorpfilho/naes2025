from django.urls import path
# Importar suas views

from .views import CategoriaCreate, SubCategoriaCreate, UsuarioCreate, ProdutoCreate, PedidoCreate, ItemPedidoCreate
from .views import CategoriaUpdate

urlpatterns = [
    path("cadastrar/categoria/", CategoriaCreate.as_view(), name="cadastrar-categoria"),
    path("cadastrar/sub-categoria/", SubCategoriaCreate.as_view(), name="cadastrar-sub-categoria"),
    path("cadastrar/produto/", ProdutoCreate.as_view(), name="cadastrar-produto"),
    path("cadastrar/pedido/", PedidoCreate.as_view(), name="cadastrar-pedido"),
     path("cadastrar/usuario/", UsuarioCreate.as_view(), name="cadastrar-usuario"),
    path("cadastrar/item-pedido/", ItemPedidoCreate.as_view(), name="cadastrar-item-pedido"),
    
    path("editar/categoria/<int:pk>/", CategoriaUpdate.as_view(), name="editar-categoria"),
    # path("listar/categoria/", CategoriaList.as_view(), name="listar-categoria"),
]
