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
        return f'{self.nome} - R${self.preco}'
    
    class Meta:
        ordering = ["nome"]
        

class TipoUsuario(models.TextChoices):
    ADMIN = 'ADMIN', 'Administrador'
    CLIENTE = 'CLIENTE', 'Cliente'
 

class Usuario(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name="usuario")
    nome = models.CharField(max_length=255)          
    endereco = models.CharField(max_length=255)   
    telefone = models.CharField(max_length=20)
    cpf = models.CharField(max_length=14, unique=True) 
    tipo = models.CharField(
        max_length=10,
        choices=TipoUsuario.choices,
        default=TipoUsuario.CLIENTE
    )

    def __str__(self):
        return f'{self.nome}'

    def clean_email(self):
        email = self.cleaned_data.get('email')
        # Verifica se o email já está sendo usado como username em auth_user
        if User.objects.filter(username=email).exists():
            raise forms.ValidationError("Este e-mail já está registrado.")
        return email
    

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
        max_length=11,
        choices=StatusPedido.choices,
        default=StatusPedido.PENDENTE
    )
    
    def __str__(self):
        return f"{self.pedido_por} - Em {self.data_pedido.strftime('%d/%m/%Y')}"

    
    
class ItemPedido(models.Model):
    pedido_por = models.ForeignKey(Usuario, on_delete=models.PROTECT)
    pedido = models.ForeignKey(Pedido, on_delete=models.PROTECT, null=True)
    produto = models.ForeignKey(Produto, on_delete=models.PROTECT)
    nome_produto = models.CharField(max_length=255)
    quantidade = models.PositiveIntegerField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"{self.pedido} - {self.produto} - {self.quantidade}"     
    

    # Adicionar usuario no itempedido, para vincular no carrinho a qual usuario ele pertence, se não todos podem ver
    # Mudado pedido para poder ser nulo, que dai vai sinalizar que esse item está no carrinho e não um pedido feito
    # Removido email do Usuário pois User ja resolve isso, assim como senha, que só estava no diagrama