from django.urls import path
# Importar suas views

from .views import CategoriaCreate
from .views import CategoriaUpdate

urlpatterns = [
    path("cadastrar/categoria/", CategoriaCreate.as_view(), name="cadastrar-categoria"),
    path("editar/categoria/<int:pk>/", CategoriaUpdate.as_view(), name="editar-categoria"),
    # path("listar/categoria/", CategoriaList.as_view(), name="listar-categoria"),
]
