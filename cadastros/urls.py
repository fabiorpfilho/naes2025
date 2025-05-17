from django.urls import path
# Importar suas views

from .views import CategoriaCreate, SubCategoriaCreate, ProdutoCreate, UsuarioCreate, PedidoCreate, ItemPedidoCreate
from .views import CategoriaUpdate, SubCategoriaUpdate, ProdutoUpdate, UsuarioUpdate, PedidoUpdate, ItemPedidoUpdate
from .views import CategoriaDelete, SubCategoriaDelete, ProdutoDelete, UsuarioDelete, PedidoDelete, ItemPedidoDelete
from .views import CategoriaList, SubCategoriaList, ProdutoList, UsuarioList, PedidoList, ItemPedidoList


urlpatterns = [
    path("cadastrar/categoria/", CategoriaCreate.as_view(), name="cadastrar-categoria"),
    path("cadastrar/sub-categoria/", SubCategoriaCreate.as_view(), name="cadastrar-sub-categoria"),
    path("cadastrar/produto/", ProdutoCreate.as_view(), name="cadastrar-produto"),
    path("cadastrar/usuario/", UsuarioCreate.as_view(), name="cadastrar-usuario"),
    path("cadastrar/pedido/", PedidoCreate.as_view(), name="cadastrar-pedido"),
    path("cadastrar/item-pedido/", ItemPedidoCreate.as_view(), name="cadastrar-item-pedido"),
    
    path("editar/categoria/<int:pk>/", CategoriaUpdate.as_view(), name="editar-categoria"),
    path("editar/sub-categoria/<int:pk>/", SubCategoriaUpdate.as_view(), name="editar-sub-categoria"),
    path("editar/produto/<int:pk>/", ProdutoUpdate.as_view(), name="editar-produto"),
    path("editar/usuario/<int:pk>/", UsuarioUpdate.as_view(), name="editar-usuario"),
    path("editar/pedido/<int:pk>/", PedidoUpdate.as_view(), name="editar-pedido"),
    path("editar/item-pedido/<int:pk>/", ItemPedidoUpdate.as_view(), name="editar-item-pedido"),
    
    path("excluir/categoria/<int:pk>/", CategoriaDelete.as_view(), name="excluir-categoria"),
    path("excluir/sub-categoria/<int:pk>/", SubCategoriaDelete.as_view(), name="excluir-sub-categoria"),
    path("excluir/produto/<int:pk>/", ProdutoDelete.as_view(), name="excluir-produto"),
    path("excluir/usuario/<int:pk>/", UsuarioDelete.as_view(), name="excluir-usuario"),
    path("excluir/pedido/<int:pk>/", PedidoDelete.as_view(), name="excluir-pedido"),
    path("excluir/item-pedido/<int:pk>/", ItemPedidoDelete.as_view(), name="excluir-item-pedido"),
    
    path("listar/categoria/", CategoriaList.as_view(), name="listar-categoria"),
    path("listar/sub-categoria/", SubCategoriaList.as_view(), name="listar-sub-categoria"),
    path("listar/produto/", ProdutoList.as_view(), name="listar-produto"),
    path("listar/usuario/", UsuarioList.as_view(), name="listar-usuario"),
    path("listar/pedido/", PedidoList.as_view(), name="listar-pedido"),
    path("listar/item-pedido/=", ItemPedidoList.as_view(), name="listar-item-pedido"),
    # path("listar/categoria/", CategoriaList.as_view(), name="listar-categoria"),
]
