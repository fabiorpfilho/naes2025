from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Categoria(models.Model):
    nome = models.CharField(max_length=120)
    descricao = models.CharField(max_length=255)
    
    def __str__(self):
        return self.nome
    
    class Meta:
        ordering = ["nome"]
    
class SubCategoria(models.Model):
    nome = models.CharField(max_length=120)
    descricao = models.CharField(max_length=255)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    
    
    def __str__(self):
        return f'{self.nome} ({self.categoria.nome})'
    
    class Meta:
        ordering = ["nome"]

class Produto(models.Model):
    nome = models.CharField(max_length=120)
    descricao = models.CharField(max_length=255)
    preco = models.DecimalField(max_digits=10, decimal_places=2)  # Ex: 12345678.90
    estoque = models.PositiveIntegerField()
    sub_categoria = models.ForeignKey(SubCategoria, on_delete=models.PROTECT)
    
    
    def __str__(self):
        return f'{self.nome} ({self.sub_categoria.nome})'
    
    class Meta:
        ordering = ["nome"]
        

class TipoUsuario(models.TextChoices):
    ADMIN = 'ADMIN', 'Administrador'
    CLIENTE = 'CLIENTE', 'Cliente'
 

class Usuario(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=255)       
    email = models.EmailField()     
    endereco = models.CharField(max_length=255)   
    telefone = models.CharField(max_length=20)
    cpf = models.CharField(max_length=14, unique=True) 
    tipo = models.CharField(
        max_length=10,
        choices=TipoUsuario.choices,
        default=TipoUsuario.CLIENTE
    )

    def __str__(self):
        return f'{self.nome} ({self.get_tipo_display()})'
    

class StatusPedido(models.TextChoices):
    PENDENTE = 'PENDENTE', 'Pendente'
    PAGO =  'PAGO', 'Pago'
    ENVIADO = 'ENVIADO', 'Enviado'
    ENTREGUE = 'ENTREGUE', 'Entregue'
    CANCELADO = 'CANCELADO', 'Cancelado'
    DEVOLVIDO = 'DEVOLVIDO', 'Devolvido'
    REEMBOLSADO = 'REEMBOLSADO', 'Reembolsado'
 

class Pedido(models.Model):
    pedido_por = models.ForeignKey(Usuario, on_delete=models.PROTECT)
    data_pedido = models.DateTimeField(auto_now_add=True)
    total= models.DecimalField(max_digits=10, decimal_places=2)  
    status = models.CharField(
        max_length=10,
        choices=StatusPedido.choices,
        default=StatusPedido.PENDENTE
    )

    
    
class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.PROTECT)
    produto = models.ForeignKey(Produto, on_delete=models.PROTECT)
    nome_produto = models.CharField(max_length=255)
    quantidade = models.PositiveIntegerField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)     
    