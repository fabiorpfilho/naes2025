from django.contrib import admin
from .models import Categoria, SubCategoria, Produto, Usuario, Pedido, ItemPedido

# Register your models here.
admin.site.register(Categoria)
admin.site.register(SubCategoria)
admin.site.register(Produto)
admin.site.register(Usuario)
admin.site.register(Pedido)
admin.site.register(ItemPedido)
